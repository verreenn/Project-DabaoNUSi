from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Profile
from theApp.models import Meal

from shopping_cart.extras import generate_order_id
from shopping_cart.models import OrderItem, Order
import datetime


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = Profile.objects.get(id=request.user.id)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
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
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary', args=[rest_id]))

@login_required()
def order_details(request, rest_id):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order,
        'rest_id': rest_id
    }
    return render(request, 'order_summary.html', context)

@login_required()
def checkout(request, order_id):
    order = Order.objects.get(id = order_id, is_ordered=False)
    order.save()
    return render(request, 'index.html')


