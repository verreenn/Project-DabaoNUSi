from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=120)

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
    food = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " at " + self.location.__str__()

    def get_avg_price(self):
        meals = Meal.objects.filter(restaurant__id=self.id)
        count = meals.count()
        if count==0:
            return 0
        else:
            return sum([meal.price for meal in meals])/count

class Meal(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name #+ " price: " + str(self.price) + " served by " + str(self.restaurant)
