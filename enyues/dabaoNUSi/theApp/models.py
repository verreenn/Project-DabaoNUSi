from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name + " at " + self.location

class Meal(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " price: " + self.price + " served by " + self.restaurant
