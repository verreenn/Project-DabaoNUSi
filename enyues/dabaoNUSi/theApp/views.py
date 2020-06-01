from django.shortcuts import render
from .models import Restaurant, Meal, Category, Location

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def home(request):
    return render(request, 'index.html')

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

def search_result(request):
    qs = Restaurant.objects.all()
    location_query = request.POST.get('location')
    category_query = request.POST.get('category')
    restaurant_name_query = request.POST.get('name')

    if location_query != '' and location_query is not None:
        qs = qs.filter(location__name__icontains=location_query)

    if category_query != '' and category_query is not None and category_query != 'Choose...':
        qs = qs.filter(categories__name=category_query)

    if restaurant_name_query != '' and restaurant_name_query is not None:
        qs = qs.filter(name__icontains=category_query)

    context = {
        'queryset' : qs
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

def help_me_dabao(request):
    return render(request, 'help-me-dabao.html')

def help_others_dabao(request):
    return render(request, 'help-others-dabao.html')

def login(request):
    return render(request, 'login.html')

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


