"""dabaoNUSi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('home/', views.home, name = 'home'),
    path('search_form/', views.search_form, name='search'),
    path('food/', views.food, name='food'),
    path('drinks/', views.drinks, name='drinks'),
    path('help_me_dabao/', views.help_me_dabao, name='help me dabao'),
    path('help_others_dabao/', views.help_others_dabao, name='help others tabao'),
    path('login/', views.login, name='login'),
    path('search_result/', views.search_result, name='search_result'),
    path('Chinese/', views.chinese, name='Chinese'),
    path('Coffee/', views.coffee, name='Coffee'),
    path('Tea/', views.tea, name='Tea'),
    path('Juice/', views.juice, name='Juice'),
    path('Korean/', views.korean, name='Korean'),
    path('Western/', views.western, name='Western'),
    path('Japanese/', views.japanese, name='Japanses'),
    path('Non_Halal/', views.non_halal, name='Non Halal'),
    path('Halal/', views.halal, name='Halal'),
    path('Utown_food/', views.utown_food, name='Utown Food'),
    path('Yih_food/', views.yih_food, name='YIH Food'),
    path('Pgp_food/', views.pgp_food, name='PGP Food'),
    path('Soc_food/', views.soc_food, name='SOC Food'),
    path('Ff_food/', views.ff_food, name='FF Food'),
    path('Flavors_food/', views.flavors_food, name='Flavors Food'),
    path('Deck_food/', views.deck_food, name='The Deck Food'),
    path('Frontier_food/', views.frontier_food, name='Frontier Food'),
    path('Utown_drink/', views.utown_drink, name='Utown Drink'),
    path('Yih_drink/', views.yih_drink, name='YIH Drink'),
    path('Pgp_drink/', views.pgp_drink, name='PGP Drink'),
    path('Soc_drink/', views.soc_drink, name='SOC Drink'),
    path('Ff_drink/', views.ff_drink, name='FF Drink'),
    path('Flavors_drink/', views.flavors_drink, name='Flavors Drink'),
    path('Deck_drink/', views.deck_drink, name='The Deck Drink'),
    path('Frontier_drink/', views.frontier_drink, name='Frontier Drink'),
]
