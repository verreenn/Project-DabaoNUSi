from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Profile
from theApp.models import Meal, Destination, Location

from shopping_cart.extras import generate_order_id
from shopping_cart.models import OrderItem, Order
import datetime


def get_user_pending_order(request, rest_id):
    # get order for the correct user
    user_profile = Profile.objects.get(id=request.user.id)
    order = Order.objects.filter(owner=user_profile, is_ordered=False, restaurant_id=rest_id)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


@login_required()
def add_to_cart(request, item_id):
    # get the user profile
    user_profile = Profile.objects.get(id=request.user.id)
    # filter products by id
    product = Meal.objects.filter(id=item_id).first()
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(meal=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    rest_id = product.restaurant.id
    return redirect(reverse('theApp:meal_list', args=[rest_id]))

@login_required()
def delete_from_cart(request, item_id, rest_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].subtract_quantity()
        if (item_to_delete[0].quantity == 0):
            item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary', args=[rest_id]))

@login_required()
def add_item(request, item_id, rest_id):
    item_to_add = OrderItem.objects.filter(pk=item_id)
    if item_to_add.exists():
        item_to_add[0].add_quantity()
        test = item_to_add[0].quantity
        messages.info(request, "Item has been added")
    #return render(request, 'index.html', {'test':test})
    return redirect(reverse('shopping_cart:order_summary', args=[rest_id]))

@login_required()
def order_details(request, rest_id):
    existing_order = get_user_pending_order(request,rest_id)
    context = {
        'order': existing_order,
        'rest_id': rest_id
    }
    return render(request, 'order_summary.html', context)

@login_required()
def checkout(request, order_id, rest_id):
    order = Order.objects.get(id = order_id, is_ordered=False)
    destinations = Destination.objects.all()
    order.save()
    context = {
        'order': order,
        'rest_id':rest_id,
        'destinations':destinations
    }
    return render(request, 'add_order_details.html', context)

def add_details(request, order_id):
    destinations = Destination.objects.all()
    locations = Location.objects.all()
    number_query = request.POST.get('number')
    details_query = request.POST.get('details')
    destination_query = request.POST.get('destination')
    order = Order.objects.get(id = order_id, is_ordered=False)
    order.number = number_query
    order.details = details_query
    order.destination = destination_query
    order.is_ordered = True
    order.save()
    context = {
        'order': order,
        'locations':locations,
        'destinations':destinations
    }
    return render(request, 'help-others-dabao.html', context)


