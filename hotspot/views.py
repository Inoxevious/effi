from django.shortcuts import render
from django.db.models import Q
from django.conf import settings
import os
from cart.cart import Cart
# Create your views here.
def placeOrder(request,hotspot_id):
    return render(request, 'pages/signup.html')

def contact_us(request,hotspot_id):
    return render(request, 'pages/signup.html')