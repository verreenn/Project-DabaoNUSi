from django.test import TestCase, Client
from django.urls import reverse, resolve
from theApp.views import about, search_form, help_me_dabao, login
from shopping_cart.views import order_details
from register.views import register_view
from shopping_cart.models import Order
from accounts.models import Profile
from theApp.models import Restaurant, Location, Category, Reviews, Price
from django.contrib.auth.models import User 

# Create your tests here.
class SimpleTests(TestCase):

#test the urls

    #test the rendering of 'about' page
    def test_about_url_is_resolved(self):
        url = reverse('theApp:about')
        self.assertEquals(resolve(url).func, about)

    #test the rendering of 'search_form' page
    def test_search_form_url_is_resolved(self):
        url = reverse('theApp:search')
        self.assertEquals(resolve(url).func, search_form)

#test the views

    #test if login requirements for some pages are working
    def test_project_help_me_dabao_GET(self):
        client = Client()
        response = client.get(reverse('theApp:help_me_dabao'))

        self.assertEquals(response.status_code, 302) #redirect because login is needed to access this page

    def test_project_about_GET(self):
        client = Client()
        response = client.get(reverse('theApp:about'))

        self.assertEquals(response.status_code, 200) # no login needed to access this page
        self.assertTemplateUsed(response, 'about-us.html')

    #test whether the login is valid
    def test_is_login_valid_view(self):
        def setUp(self):
            self.credentials = {
                'username': 'testuser',
                'password': 'secret098765'
            }
            User.objects.create_user(**self.credentials)
        def test_login(self):
            response = self.client.post('/accounts/login/', self.credentials, follow=True)
            self.assertTrue(response.context['user'].is_active)

    #test whether registration is valid
    def test_is_registration_valid(self):
        def setUp(self):
            self.username = 'testuser'
            self.email = 'testuser@email.com'
            self.password1 = 'neanderthal1999'
            self.password2 = 'neanderthal1999'
            self.phone = '90908767'

        def test_signup_page_url(self):
            response = self.client.get("/accounts/register/")
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, template_name='register.html')

        def test_signup_page_view_name(self):
            response = self.client.get(reverse('accounts:register'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, template_name='register.html')

        def test_signup_form(self):
            response = self.client.post(reverse('accounts:register'), data={
                'username': self.username,
                'email': self.email,
                'phone': self.phone,
                'password1': self.password,
                'password2': self.password
            })
            self.assertEqual(response.status_code, 200)

            users = get_user_model().objects.all()
            self.assertEqual(users.count(), 1)

    



