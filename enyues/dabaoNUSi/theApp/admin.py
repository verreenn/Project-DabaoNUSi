from django.contrib import admin

# Register your models here.
from .models import Location, Meal, Restaurant, Category, Comment, Rate, Reviews, Price, Dietary, Other, Destination

admin.site.register(Location)
admin.site.register(Meal)
admin.site.register(Reviews)
admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rate)
admin.site.register(Price)
admin.site.register(Dietary)
admin.site.register(Other)
admin.site.register(Destination)