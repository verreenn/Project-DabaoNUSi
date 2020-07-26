from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Meal, Category, Location, Reviews, Price, Dietary, Other, Destination, Comment, Rate
from accounts.models import Profile
from shopping_cart.models import Order
from django.urls import reverse
from .forms import CommentForm, RateForm
#rom shopping_cart.models import Order
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'index.html', {'restaurants' : restaurants})

def about(request):
    return render(request, 'about-us.html')

def home(request):
    restaurants = Restaurant.objects.all()
    orders = Order.objects.all()
    return render(request, 'index.html',{'restaurants' : restaurants, 'orders': orders})

def arise(request):
    rest = Restaurant.objects.filter(name__icontains="arise").first()
    return meal_list(request, rest.id)

def atempo(request):
    rest = Restaurant.objects.filter(name__icontains="atempo").first()
    return meal_list(request, rest.id)

def barbar(request):
    rest = Restaurant.objects.filter(name__icontains="bar").first()
    return meal_list(request, rest.id)

def crave(request):
    rest = Restaurant.objects.filter(name__icontains="crave").first()
    return meal_list(request, rest.id)

def hwangs(request):
    rest = Restaurant.objects.filter(name__icontains="hwang").first()
    return meal_list(request, rest.id)

def sinkee(request):
    return render(request, 'sinkee.html')

def yongtaufoo(request):
    return render(request, 'yongtaufoo.html')

def cool_spot(request):
    rest = Restaurant.objects.filter(name__icontains="cool").first()
    return meal_list(request, rest.id)

def spinelli(request):
    rest = Restaurant.objects.filter(name__icontains="spinelli").first()
    return meal_list(request, rest.id)

def maxx_coffee(request):
    rest = Restaurant.objects.filter(name__icontains="maxx").first()
    return meal_list(request, rest.id)

def liho(request):
    rest = Restaurant.objects.filter(name__icontains="liho").first()
    return meal_list(request, rest.id)

def gongcha(request):
    rest = Restaurant.objects.filter(name__icontains="gong cha").first()
    return meal_list(request, rest.id)

def fass_mala(request):
    rest = Restaurant.objects.filter(name__icontains="liang ban").first()
    return meal_list(request, rest.id)

def teaparty(request):
    rest = Restaurant.objects.filter(name__icontains="tea party").first()
    return meal_list(request, rest.id)

def subway(request):
    rest = Restaurant.objects.filter(name__icontains="subway").first()
    return meal_list(request, rest.id)

def ichiban(request):
    rest = Restaurant.objects.filter(name__icontains="taiwan ichiban").first()
    return meal_list(request, rest.id)

def pasta_express(request):
    rest = Restaurant.objects.filter(name__icontains="pasta express").first()
    return meal_list(request, rest.id)

def deck_juice(request):
    rest = Restaurant.objects.filter(name__icontains="juice").first()
    return meal_list(request, rest.id)

def liji(request):
    rest = Restaurant.objects.filter(name__icontains="liji").first()
    return meal_list(request, rest.id)

def the_coffee_roaster(request):
    rest = Restaurant.objects.filter(name__icontains="coffee roaster").first()
    return meal_list(request, rest.id)

def jewel_coffee(request):
    rest = Restaurant.objects.filter(name__icontains="jewel").first()
    return meal_list(request, rest.id)

def starbucks(request):
    rest = Restaurant.objects.filter(name__icontains="starbucks").first()
    return meal_list(request, rest.id)
    
def food2(request):
    return render(request, 'food2.html')

def drinks2(request):
    return render(request, 'drinks2.html')

def search_result(request):
    qs = Restaurant.objects.all()
    location_query = request.POST.get('location')
    category_query = request.POST.get('category')
    restaurant_name_query = request.POST.get('name')
    sort_query = request.GET.get('sort', 'id')
    sort_query = request.POST.get('sort')
    rating_query = request.POST.get('rating')
    prices_query = request.POST.get('prices')

    if location_query != '' and location_query is not None:
        qs = qs.filter(location__name__icontains=location_query)

    if category_query != '' and category_query is not None and category_query != 'Choose...':
        qs = qs.filter(categories__name=category_query)

    if restaurant_name_query != '' and restaurant_name_query is not None:
        qs = qs.filter(name__icontains=restaurant_name_query)

    if rating_query != '' and rating_query is not None and rating_query != 'Choose...':
        if rating_query == "More Than 1 Star":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_rating() >= 1]
            qs = qs.filter(id__in=rest_ids)
        elif rating_query == "More Than 2 Stars":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_rating() >= 2]
            qs = qs.filter(id__in=rest_ids)
        elif rating_query == "More Than 3 Stars":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_rating() >= 3]
            qs = qs.filter(id__in=rest_ids)
        elif rating_query == "More Than 4 Stars":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_rating() >= 4]
            qs = qs.filter(id__in=rest_ids)
        elif rating_query == "5 Stars":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_rating() == 5]
            qs = qs.filter(id__in=rest_ids)
    
    if prices_query != '' and prices_query is not None and prices_query != 'Choose...':
        if prices_query == "Less Than $5":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_price() <= 5]
            qs = qs.filter(id__in=rest_ids)
        elif prices_query == "Less Than $10":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_price() <= 10]
            qs = qs.filter(id__in=rest_ids)
        elif prices_query == "Less Than $20":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_price() <= 20]
            qs = qs.filter(id__in=rest_ids)

    rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_price() <= 5]

    if sort_query != '' and sort_query is not None and sort_query != 'Choose...':
        if sort_query == 'average_price_desc':
            qs = sorted(qs, key=lambda a: a.get_avg_price(), reverse=True)
        elif sort_query == 'average_price_asc':
            qs = sorted(qs, key=lambda a: a.get_avg_price(), reverse=False)
        elif sort_query == 'average_rating_desc':
            qs = sorted(qs, key=lambda a: a.get_avg_rating(), reverse=True)
        elif sort_query == 'average_rating_asc':
            qs = sorted(qs, key=lambda a: a.get_avg_rating(), reverse=False)

    context = {
        'queryset' : qs,
    }

    return render(request, "search_result.html", context)

def food(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'food.html', {'categories':categories,
    'locations':locations})

def drinks(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'drinks.html', {'categories':categories,
    'locations':locations})

@login_required()
def help_me_dabao(request):
    locations = Location.objects.all()
    reviews = Reviews.objects.all()
    prices = Price.objects.all()
    dietarys = Dietary.objects.all()
    others = Other.objects.all()
    return render(request, 'help-me-dabao.html', {'locations':locations, 'reviews':reviews, 'prices':prices, 'dietarys':dietarys, 'others':others})

@login_required()
def help_others_dabao(request):
    locations = Location.objects.all()
    destinations = Destination.objects.all()
    orders = Order.objects.filter(is_ordered=True, is_helped=False, timeEnd__gte=datetime.now())
    return render(request, 'help-others-dabao.html', {'locations':locations, 'destinations':destinations, 'orders':orders})

def help_others_dabao_result(request):
    qs = Order.objects.all()
    location_query = request.POST.get('location')
    orders = Order.objects.filter(is_ordered=True, is_helped=False, timeEnd__gte=datetime.now())
    if location_query != '' and location_query is not None and location_query != 'Choose...':
        qs = qs.filter(location__name__icontains=location_query)

    context = {
        'queryset' : qs
    }

    return render(request, "help_others_dabao_result.html", context)

def login_test(request):
    return render(request, "login_test.html")

@login_required()
def login(request):
    return render(request, 'login.html')

def search_form(request):
    categories = Category.objects.all()
    reviews = Reviews.objects.all()
    prices = Price.objects.all()
    return render(request, 'search_form.html', {'categories':categories, 'ratings':reviews, 'prices':prices})

def chinese(request):
    qs = Restaurant.objects.filter(categories__name='Chinese')
    return render(request, "search_result.html", {'queryset':qs})

def coffee(request):
    qs = Restaurant.objects.filter(categories__name='Coffee')
    return render(request, "search_result.html", {'queryset':qs})

def tea(request):
    qs = Restaurant.objects.filter(categories__name='Tea')
    return render(request, "search_result.html", {'queryset':qs})

def juice(request):
    qs = Restaurant.objects.filter(categories__name='Juice')
    return render(request, "search_result.html", {'queryset':qs})

def korean(request):
    qs = Restaurant.objects.filter(categories__name='Korean')
    return render(request, "search_result.html", {'queryset':qs})

def western(request):
    qs = Restaurant.objects.filter(categories__name='Western')
    return render(request, "search_result.html", {'queryset':qs})

def japanese(request):
    qs = Restaurant.objects.filter(categories__name='Japanese')
    return render(request, "search_result.html", {'queryset':qs})

def non_halal(request):
    qs = Restaurant.objects.filter(categories__name='Non Halal')
    return render(request, "search_result.html", {'queryset':qs})

def halal(request):
    qs = Restaurant.objects.filter(categories__name='Halal')
    return render(request, "search_result.html", {'queryset':qs})

def utown_food(request):
    qs = Restaurant.objects.filter(location__name__icontains='University Town').filter(food=True)
    return render(request, "search_result.html", {'queryset':qs})

def ff_food(request):
    qs = Restaurant.objects.filter(location__name__icontains='Fine Food University Town').filter(food=True)
    return render(request, "search_result.html", {'queryset':qs})

def yih_food(request):
    qs = Restaurant.objects.filter(location__name__icontains='Yusof Ishak House').filter(food=True)
    return render(request, "search_result.html", {'queryset':qs})

def pgp_food(request):
    qs = Restaurant.objects.filter(location__name__icontains='PGP').filter(food=True)
    return render(request, "search_result.html", {'queryset':qs})

def soc_food(request):
    qs = Restaurant.objects.filter(location__name__icontains='School of Computing').filter(food=True)
    return render(request, "search_result.html", {'queryset':qs})

def flavors_food(request):
    qs = Restaurant.objects.filter(location__name__icontains='Flavors University Town').filter(food=True)
    return render(request, "search_result.html", {'queryset':qs})

def deck_food(request):
    qs = Restaurant.objects.filter(location__name__icontains='FASS The Deck').filter(food=True)
    return render(request, "search_result.html", {'queryset':qs})

def frontier_food(request):
    qs = Restaurant.objects.filter(location__name__icontains='Faculty of Science Frontier').filter(food=True)
    return render(request, "search_result.html", {'queryset':qs})

def utown_drink(request):
    qs = Restaurant.objects.filter(location__name__icontains='University Town').filter(food=False)
    return render(request, "search_result.html", {'queryset':qs})

def ff_drink(request):
    qs = Restaurant.objects.filter(location__name__icontains='Fine Food University Town').filter(food=False)
    return render(request, "search_result.html", {'queryset':qs})

def yih_drink(request):
    qs = Restaurant.objects.filter(location__name__icontains='Yusof Ishak House').filter(food=False)
    return render(request, "search_result.html", {'queryset':qs})

def pgp_drink(request):
    qs = Restaurant.objects.filter(location__name__icontains='PGP').filter(food=False)
    return render(request, "search_result.html", {'queryset':qs})

def soc_drink(request):
    qs = Restaurant.objects.filter(location__name__icontains='School of Computing').filter(food=False)
    return render(request, "search_result.html", {'queryset':qs})

def flavors_drink(request):
    qs = Restaurant.objects.filter(location__name__icontains='Flavors University Town').filter(food=False)
    return render(request, "search_result.html", {'queryset':qs})

def deck_drink(request):
    qs = Restaurant.objects.filter(location__name__icontains='FASS The Deck').filter(food=False)
    return render(request, "search_result.html", {'queryset':qs})

def frontier_drink(request):
    qs = Restaurant.objects.filter(location__name__icontains='Faculty of Science Frontier').filter(food=False)
    return render(request, "search_result.html", {'queryset':qs})

def meal_list(request, rest_id):
    meals = Meal.objects.filter(restaurant__id=rest_id)
    rest = Restaurant.objects.filter(id=rest_id).first()
    comments = Comment.objects.filter(restaurant__id=rest_id)[:5]
    form_comment = CommentForm()
    form_rating = RateForm()
    return render(request, "restaurant_meals.html", {
        'meals':meals,
        'rest':rest,
        'form_rating':form_rating,
        'form_comment':form_comment,
        'comments':comments
        })

def confirmation(request, order_id):
    orders = Order.objects.filter(id=order_id)
    order = orders.first()
    order.is_helped = True
    order.save()
    return render(request, 'confirmation.html', {'orders':orders})

def order_detail(request, order_id):
    order = Order.objects.filter(id=order_id).first()
    meals = order.get_cart_items
    return render(request, "order_detail.html", {
        'order':order,
        'meals':meals
        })

def add_comment(request, rest_id):
    restaurant = get_object_or_404(Restaurant, id=rest_id)
    user_profile = Profile.objects.get(user__username=request.user.username)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.restaurant = restaurant
            comment.user = user_profile
            comment.save()
    return redirect('theApp:meal_list', rest_id=rest_id)
    
def add_rating(request, rest_id):
    restaurant = get_object_or_404(Restaurant, id=rest_id)
    user_profile = Profile.objects.get(user__username=request.user.username)
    rate = Rate.objects.create(restaurant=restaurant, user=user_profile)
    rating = request.POST['rating']
    rate.rating = rating
    rate.save()
    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.restaurant = restaurant
            rate.user = user_profile
            rate.save()
    #return render(request, 'index.html',{'test':rating})
    return redirect('theApp:meal_list', rest_id=rest_id)

def help_me_dabao_search(request):
    keyword_query = request.POST.get('keyword')
    prices_query = request.POST.get('price')
    location_query = request.POST.get('location')
    rating_query = request.POST.get('reviews')
    dietarys_query = request.POST.get('dietarys')
    others_query = request.POST.get('others')
    qs = Restaurant.objects.all()

    if location_query != '' and location_query is not None and location_query != "LOCATION":
        qs = qs.filter(location__name__icontains=location_query)

    if dietarys_query != '' and dietarys_query is not None and dietarys_query != "DIETARY NEEDS":
        qs = qs.filter(categories__name=dietarys_query)

    if others_query != '' and others_query is not None and others_query != "OTHERS":
        qs = qs.filter(categories__name=others_query)

    if keyword_query != '' and keyword_query is not None:
        qs = qs.filter(name__icontains=keyword_query)

    if rating_query != '' and rating_query is not None and rating_query != 'REVIEW':
        if rating_query == "More Than 1 Star":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_rating() >= 1]
            qs = qs.filter(id__in=rest_ids)
        elif rating_query == "More Than 2 Stars":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_rating() >= 2]
            qs = qs.filter(id__in=rest_ids)
        elif rating_query == "More Than 3 Stars":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_rating() >= 3]
            qs = qs.filter(id__in=rest_ids)
        elif rating_query == "More Than 4 Stars":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_rating() >= 4]
            qs = qs.filter(id__in=rest_ids)
        elif rating_query == "5 Stars":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_rating() == 5]
            qs = qs.filter(id__in=rest_ids)
    
    if prices_query != '' and prices_query is not None and prices_query != 'PRICE':
        if prices_query == "Less Than $5":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_price() <= 5]
            qs = qs.filter(id__in=rest_ids)
        elif prices_query == "Less Than $10":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_price() <= 10]
            qs = qs.filter(id__in=rest_ids)
        elif prices_query == "Less Than $20":
            rest_ids = [rest.id for rest in Restaurant.objects.all() if rest.get_avg_price() <= 20]
            qs = qs.filter(id__in=rest_ids)


    context = {'price':prices_query,
    'loc':location_query,
    'rev':rating_query,
    'diet':dietarys_query,
    'ot':others_query,
    'queryset':qs}

    return render(request, "help_me_dabao_result.html", context)

def food_search(request):
    qs = Restaurant.objects.filter(food=True)
    restaurant_name_query = request.POST.get('name')

    if restaurant_name_query != '' and restaurant_name_query is not None:
        qs = qs.filter(name__icontains=restaurant_name_query)

    context = {
        'queryset' : qs,
    }

    return render(request, "search_result.html", context)

def drink_search(request):
    qs = Restaurant.objects.filter(food=False)
    restaurant_name_query = request.POST.get('name')

    if restaurant_name_query != '' and restaurant_name_query is not None:
        qs = qs.filter(name__icontains=restaurant_name_query)

    context = {
        'queryset' : qs,
    }

    return render(request, "search_result.html", context)