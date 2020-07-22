from django.test import TestCase
from django.urls import reverse, resolve
from theApp.views import about, search_form, help_me_dabao, login
from shopping_cart.views import order_details_test
from shopping_cart.models import Order
from accounts.models import Profile
from theApp.models import Restaurant, Location, Category, Reviews, Price

# Create your tests here.
class SimpleTests(TestCase):

    #test the rendering of 'about' page
    def test_about_url_is_resolved(self):
        url = reverse('theApp:about')
        self.assertEquals(resolve(url).func, about)

    #test the rendering of 'search_form' page
    def test_search_form_url_is_resolved(self):
        url = reverse('theApp:search')
        self.assertEquals(resolve(url).func, search_form)

    #test the rendering of 'login' page
    def test_login_url_is_resolved(self):
        url = reverse('theApp:login')
        self.assertEquals(resolve(url).func, login)

    #test the functionality of @login_required
    def test_login_requirement(self):
        url = reverse('theApp:help_me_dabao')
        self.assertEquals(resolve(url).func, help_me_dabao)

