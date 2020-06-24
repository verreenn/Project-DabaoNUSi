from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Meal, Category, Location, Reviews, Price, Dietary, Other, Destination
from accounts.models import Profile
from shopping_cart.models import Order
from .forms import CommentForm, RateForm
#rom shopping_cart.models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'index.html', {'restaurants' : restaurants, 'test':"test"})

def about(request):
    return render(request, 'about-us.html')

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'index.html',{'restaurants' : restaurants, 'test':"test"})

def arise(request):
    return render(request, 'arise.html')

def atempo(request):
    return render(request, 'atempo.html')

def barbar(request):
    return render(request, 'barbar.html')

def crave(request):
    return render(request, 'crave.html')

def hwangs(request):
    return render(request, 'hwangs.html')

def sinkee(request):
    return render(request, 'sinkee.html')

def yongtaufoo(request):
    return render(request, 'yongtaufoo.html')

def cool_spot(request):
    return render(request, 'cool_spot.html')

def spinelli(request):
    return render(request, 'spinelli.html')

def maxx_coffee(request):
    return render(request, 'maxx_coffee.html')

def liho(request):
    return render(request, 'liho.html')

def gongcha(request):
    return render(request, 'gongcha.html')

def fass_mala(request):
    return render(request, 'fass_mala.html')

def teaparty(request):
    return render(request, 'teaparty.html')

def subway(request):
    return render(request, 'subway.html')

def ichiban(request):
    return render(request, 'ichiban.html')

def pasta_express(request):
    return render(request, 'pasta_express.html')

def deck_juice(request):
    return render(request, 'deck_juice.html')

def liji(request):
    return render(request, 'liji.html')

def the_coffee_roaster(request):
    return render(request, 'the_coffee_roaster.html')

def jewel_coffee(request):
    return render(request, 'jewel_coffee.html')

def starbucks(request):
    return render(request, 'starbucks.html')
    
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

    if location_query != '' and location_query is not None:
        qs = qs.filter(location__name__icontains=location_query)

    if category_query != '' and category_query is not None and category_query != 'Choose...':
        qs = qs.filter(categories__name=category_query)

    if restaurant_name_query != '' and restaurant_name_query is not None:
        qs = qs.filter(name__icontains=category_query)

    if sort_query == 'average_price':
        qs = sorted(qs, key=lambda a: a.get_avg_price(), reverse=True)
    elif sort_query == 'average_rating':
        qs = sorted(qs, key=lambda a: a.get_avg_rating(), reverse=True)

    test = sort_query == 'average_rating'
    context = {
        'queryset' : qs,
        'test':test
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

#@login_required()
def help_me_dabao(request):
    locations = Location.objects.all()
    reviews = Reviews.objects.all()
    prices = Price.objects.all()
    dietarys = Dietary.objects.all()
    others = Other.objects.all()
    return render(request, 'help-me-dabao.html', {'locations':locations, 'reviews':reviews, 'prices':prices, 'dietarys':dietarys, 'others':others})

#@login_required()
def help_others_dabao(request):
    locations = Location.objects.all()
    destinations = Destination.objects.all()
    return render(request, 'help-others-dabao.html', {'locations':locations, 'destinations':destinations})

def help_others_dabao_result(request):
    qs = Order.objects.all()
    location_query = request.POST.get('location')

    if location_query != '' and location_query is not None and location_query != 'Choose...':
        qs = qs.filter(location__name__icontains=location_query)

    context = {
        'queryset' : qs
    }

    return render(request, "help_others_dabao_result.html", context)

@login_required()
def login(request):
    return render(request, 'login_old.html')

def search_form(request):
    categories = Category.objects.all()
    return render(request, 'search_form.html', {'categories':categories})

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
    form_comment = CommentForm()
    form_rating = RateForm()
    return render(request, "restaurant_meals.html", {
        'meals':meals,
        'rest':rest,
        'form_rating':form_rating,
        'form_comment':form_comment
        })

def order_detail(request, order_id):
    order = Order.objects.filter(id=order_id).first()
    meals = order.get_cart_items
    return render(request, "order_detail.html", {
        'order':order,
        'meals':meals
        })

def add_comment(request, rest_id):
    restaurant = get_object_or_404(Restaurant, id=rest_id)
    user_profile = Profile.objects.get(id=request.user.id)
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
    user_profile = Profile.objects.get(id=request.user.id)
    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.restaurant = restaurant
            rate.user = user_profile
            rate.save()
    return redirect('theApp:meal_list', rest_id=rest_id)