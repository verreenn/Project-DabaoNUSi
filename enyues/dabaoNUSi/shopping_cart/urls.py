  
from django.conf.urls import url
from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
)

urlpatterns = [
    url(r'^add-to-cart/(?P<item_id>\d+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/(?P<rest_id>\d+)/$', order_details, name="order_summary"),
    url(r'^item/delete/(?P<item_id>[-\w]+)/(?P<rest_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^checkout/(?P<order_id>\d+)/$', checkout, name="checkout"),
]