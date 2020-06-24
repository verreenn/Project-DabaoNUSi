from django.db import models
from accounts.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Dietary(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Other(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Price(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    #reviews = models.ForeignKey(Reviews, on_delete = models.CASCADE, default= "More Than 1 Star")
    #prices = models.ForeignKey(Price, on_delete = models.CASCADE, default="Less Than $20")
    categories = models.ManyToManyField(Category)
    food = models.BooleanField(default=True)
    average_price = models.FloatField(default=0)
    average_rating = models.FloatField(default=0)

    def __str__(self):
        return self.name + " at " + self.location.__str__()

    def get_avg_price(self):
        meals = Meal.objects.filter(restaurant__id=self.id)
        count = meals.count()
        if count==0:
            return 0
        else:
            return sum([meal.price for meal in meals])/count

    def get_avg_rating(self):
        ratings = Rate.objects.filter(restaurant__id=self.id)
        count = ratings.count()
        if count == 0:
            return 0
        else:
            return sum([rate.rating for rate in ratings])/count
    
    average_price = get_avg_price
    average_rating = get_avg_rating

class Meal(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name #+ " price: " + str(self.price) + " served by " + str(self.restaurant)

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.user.user.username

class Rate(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.user.user.username


