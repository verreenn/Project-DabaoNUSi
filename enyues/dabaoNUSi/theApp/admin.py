from django.contrib import admin

# Register your models here.
from .models import Location, Meal, Restaurant, Category

admin.site.register(Location)
admin.site.register(Meal)
admin.site.register(Restaurant)
admin.site.register(Category)