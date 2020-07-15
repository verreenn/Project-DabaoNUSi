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
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('home/', views.home, name = 'home'),
    path('search_form/', views.search_form, name='search'),
    path('food/', views.food, name='food'),
    path('drinks/', views.drinks, name='drinks'),
    path('help_me_dabao/', views.help_me_dabao, name='help_me_dabao'),
    path('help_others_dabao/', views.help_others_dabao, name='help others tabao'),
    path('login/', views.login, name='login'),
    path('login_test/', views.login_test, name='login_test'),
    path('arise/', views.arise, name='arise'),
    path('atempo/', views.atempo, name='atempo'),
    path('barbar/', views.barbar, name='barbar'),
    path('crave/', views.crave, name='crave'),
    path('hwangs/', views.hwangs, name='hwangs'),
    path('sinkee/', views.sinkee, name='sinkee'),
    path('yongtaufoo/', views.yongtaufoo, name='yongtaufoo'),
    path('cool_spot/', views.cool_spot, name='cool_spot'),
    path('spinelli/', views.spinelli, name='spinelli'),
    path('maxx_coffee/', views.maxx_coffee, name='maxx_coffee'),
    path('liho/', views.liho, name='liho'),
    path('gongcha/', views.gongcha, name='gongcha'),
    path('pasta_express/', views.pasta_express, name='pasta_express'),
    path('deck_juice/', views.deck_juice, name='deck_juice'),
    path('starbucks/', views.starbucks, name='starbucks'),
    path('teaparty/', views.teaparty, name='teaparty'),
    path('subway/', views.subway, name='subway'),
    path('liji/', views.liji, name='liji'),
    path('jewel_coffee/', views.jewel_coffee, name='jewel_coffee'),
    path('the_coffee_roaster/', views.the_coffee_roaster, name='the_coffee_roaster'),
    path('fass_mala/', views.fass_mala, name='fass_mala'),
    path('ichiban/', views.ichiban, name='ichiban'),
    path('food2/', views.food2, name='food2'),
    path('drinks2/', views.drinks2, name='drinks2'),
    path('search_result/', views.search_result, name='search_result'),
    path('help_others_dabao_result/', views.help_others_dabao_result, name='help_others_dabao_result'),
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
    url(r'^restaurant/(?P<rest_id>\d+)/$', views.meal_list, name='meal_list'),
    url(r'^order/(?P<order_id>\d+)/$', views.order_detail, name='order_detail'),
    url(r'^restaurant/(?P<rest_id>\d+)/add_comment/$', views.add_comment, name='add_comment'),
    url(r'^restaurant/(?P<rest_id>\d+)/add_rating/$', views.add_rating, name='add_rating'),
    path('help-me-dabao/search/search/', views.help_me_dabao_search, name='help_me_dabao_search')
]
