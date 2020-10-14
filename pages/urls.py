from django.conf.urls import url
from django.urls import path, include
from .views import *
# SET THE NAMESPACE!
app_name = 'pages'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[

    path('index/', index, name='index'),
    # path('register/', register, name='register'),
    path('guide/', guide, name='guide'),
    path('listing/', listing, name='listing'),
    path('contact/', contact, name='contact'),
    path('listing/', listing, name='listing'),
    path('primary/', primary, name='primary'),
    path('secondary/', secondary, name='secondary'),
    path('faq/', faq, name='faq'),
   
]