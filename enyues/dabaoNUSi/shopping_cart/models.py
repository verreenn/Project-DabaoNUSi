from __future__ import unicode_literals
from django.db import models
from django.db import models

from accounts.models import Profile
from theApp.models import Meal, Restaurant, Destination


class OrderItem(models.Model):
    meal = models.OneToOneField(Meal, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.meal.name

    def get_total(self):
        return self.meal.price * self.quantity

    def add_quantity(self):
        self.quantity += 1
        self.save()

    def subtract_quantity(self):
        self.quantity -= 1
        self.save()


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    is_helped = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    number = models.CharField(max_length=15, default="No number provided")
    details = models.CharField(max_length=1000, default="No details provided")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default = 1)
    destination = models.CharField(max_length=100)

    def get_cart_items(self):
        return self.items.all()

    def get_restaurant(self):
        return self.items.all().first().meal.restaurant.name

    def get_restaurant_id(self):
        return self.items.all().first().meal.restaurant.id

    def get_cart_total(self):
        total = 0
        for item in self.items.all():
            total += item.get_total()
        return total

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)

    def get_handphone_number(self):
        return self.number
    
    def get_notes(self):
        return self.details