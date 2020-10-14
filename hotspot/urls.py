from django.urls import path, include # new

from .views import *
app_name = 'hotspot'

urlpatterns = [
    path('<int:hotspot_id>/place_order/', placeOrder, name='place_order'),
    path('<int:hotspot_id>/contact_us/', placeOrder, name='contact_us'),
]