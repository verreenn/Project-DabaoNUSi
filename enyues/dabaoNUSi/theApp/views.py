from django.shortcuts import render
from .models import Restaurant, Meal

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def home(request):
    return render(request, 'index.html')

def BootstrapFilterView(request):
    qs = Restaurant.objects.all()
    location_query = request.GET.get('location')
    category_query = request.GET.get('category')

    if location_query != '' and location_query is not None:
        qs = qs.filter(location__name__icontains=location_query)

    if category_query != '' and category_query is not None:
        qs = qs.filter(categories__name=category_query)

    context = {
        'queryset' : qs
    }

    return render(request, "bootstrap_form.html", context)

def food(request):
    return render(request, 'food.html')

def drinks(request):
    return render(request, 'drinks.html')

def help_me_dabao(request):
    return render(request, 'help-me-dabao.html')

def help_others_dabao(request):
    return render(request, 'help-others-dabao.html')

def login(request):
    return render(request, 'login.html')
