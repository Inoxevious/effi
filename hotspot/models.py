from django.db import models
from django.db import models
from django.core.files import File
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.hashers import get_hasher, identify_hasher
import uuid
from django.contrib.auth.models import User

class Hotspot(models.Model):

  Meters = 'Meters'
  Kilograms = 'Kilograms'
  Liters = 'Liters'
  Mililitres = "Mililitres"
  pickupPoint = 'pickupPoint'
  intransit = 'intransit'
  delivered = 'delivered'
  returning = 'returning'
  returned = 'returned'
  Gweru = 'Gweru'
  Harare = 'Harare'
  Mutare = 'Mutare'
  Bulawayo = 'Bulawayo'
  Victoria_Falls = 'Victoria Falls'
  Beitbridge = 'Beitbridge'
  Zimbabwe = 'Zimbabwe'
  Zambia = 'Zambia'
  COURIER_CHOICES = [
        (pickupPoint,'pickupPoint'),
        (intransit,'intransit'),
        (delivered,'delivered'),
        (returning,'returning'),
        (returned,'returned'),
    ]
  MEASURE_CHOICES = [
        (Meters,'Meters'),
        (Kilograms,'Kilograms'),
        (Liters,'Liters'),
        (Mililitres,'Mililitres'),
    ]
  COUNTRY_CHOICES = [
        (Zimbabwe,'Zimbabwe'),
        (Zambia,'Zambia'),

    ]
  CITY_CHOICES = [
        (Gweru,'Gweru'),
        (Harare,'Harare'),
        (Mutare,'Mutare'),
        (Bulawayo,'Bulawayo'),
        (Victoria_Falls,'Victoria_Falls'),
        (Beitbridge,'Beitbridge'),

    ]
  manager = models.OneToOneField(User, on_delete=models.CASCADE)
  reference = models.CharField(max_length=100,db_index=True)
  current_volume = models.CharField(max_length=100, null=True, blank=True)
  capacity = models.CharField(max_length=100, null=True, blank=True, choices=MEASURE_CHOICES, default = Kilograms )
  qrCode = models.CharField(max_length=100, null=True, blank=True, db_index=True)
  picture = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
  available = models.BooleanField(default=True)
  courierState  = models.CharField(max_length=100, null=True, blank=True, choices=COURIER_CHOICES, default = pickupPoint)
  location = models.PointField(null=True, blank=True)
  city = models.CharField(max_length=100, null=True, blank=True, choices=CITY_CHOICES, default = Gweru)
  residence = models.CharField(max_length=100, null=True, blank=True)
  neigbhourhood = models.CharField(max_length=100, null=True, blank=True)
  isActive = models.BooleanField(default=True)
  country = models.CharField(max_length=100, null=True, blank=True, choices=COUNTRY_CHOICES, default = Zimbabwe)

  class Meta:
      verbose_name = ('Hotspot')
      verbose_name_plural = ('Hotspots')
  def __str__(self):
    return self.reference
  # ## Geocode using full address
  # def _get_full_address(self):
  #     return u'%s %s %s %s %s %s' % (self.residence, self.city , self.country, self.zipcode)
  # full_address = property(_get_full_address)

  # ## Geocode by just using zipcode and country name (faster and more reliable)
  # def _get_geo_address(self):
  #     return u'%s %s' % (self.country.name)
  # geo_address = property(_get_geo_address)


  # def save(self, *args, **kwargs):
  #     if not self.location:
  #           if self.city and self.country:
  #               location = location = '+'.join(filter(None, ( self.residence, self.city, self.country)))
  #               self.location = get_lat_lng(location)
  #     super(Hotspot, self).save(*args, **kwargs)

class AppVersion(models.Model):
  file =  models.FileField(blank=False, null=False)
  version_name = models.CharField(max_length=100, null=True, blank=True,db_index=True)
  app_version = models.CharField(max_length=100, null=True, blank=True,db_index=True)
  app_upload_date = models.DateTimeField()
  app_expire_date = models.DateTimeField()
  class Meta:
      verbose_name = ('AppVersion')
      verbose_name_plural = ('AppVersion')
  def __str__(self):
    return self.version_name

class ActiveHotspot(models.Model):
  hotspot = models.OneToOneField(Hotspot, on_delete=models.CASCADE)
  desiel_pump = models.BooleanField(default=True)
  desiel_pump_price = models.FloatField(max_length=100, null=True, blank=True)
  petrol_pump = models.BooleanField(default=True)
  petrol_pump_price = models.FloatField(max_length=100, null=True, blank=True)
  gas_pump =  models.BooleanField(default=True)
  gas_pump_price = models.FloatField(max_length=100, null=True, blank=True)

class Orders(models.Model):
  petrol = 'petrol'
  disiel = 'disiel'
  gas = 'gas'
  FUEL_CHOICES = [
      (petrol, 'petrol'),
      (disiel,'disiel'),
      (gas,'gas'),

  ]
  hotspot = models.ManyToManyField(Hotspot)
  customer = models.ManyToManyField(User)
  fuel_type = models.CharField(max_length=100, null=True, blank=True, choices=FUEL_CHOICES, default = petrol)
  quantity = models.FloatField(max_length=100, null=True, blank=True)
  order_placed_date = models.DateTimeField(auto_now=True)
  order_pickup_date = models.DateTimeField()
  order_expire_date = models.DateTimeField()

class OrdersDelivery(models.Model):

  pickupPoint = 'pickupPoint'
  intransit = 'intransit'
  delivered = 'delivered'
  returning = 'returning'
  returned = 'returned'
  Gweru = 'Gweru'
  Harare = 'Harare'
  Mutare = 'Mutare'
  Bulawayo = 'Bulawayo'
  Victoria_Falls = 'Victoria Falls'
  Beitbridge = 'Beitbridge'
  Zimbabwe = 'Zimbabwe'
  Zambia = 'Zambia'
  COURIER_CHOICES = [
        (pickupPoint,'pickupPoint'),
        (intransit,'intransit'),
        (delivered,'delivered'),
        (returning,'returning'),
        (returned,'returned'),
    ]
  CITY_CHOICES = [
    (Gweru,'Gweru'),
    (Harare,'Harare'),
    (Mutare,'Mutare'),
    (Bulawayo,'Bulawayo'),
    (Victoria_Falls,'Victoria_Falls'),
    (Beitbridge,'Beitbridge'),

    ]
  order = models.ManyToManyField(Orders)
  order_delivery_date = models.DateTimeField()
  order_delivery_courierState  = models.CharField(max_length=100, null=True, blank=True, choices=COURIER_CHOICES, default = pickupPoint)
  order_delivery_location = models.PointField(null=True, blank=True)
  order_delivery_city = models.CharField(max_length=100, null=True, blank=True, choices=CITY_CHOICES, default = Gweru)
  order_delivery_residence = models.CharField(max_length=100, null=True, blank=True)
  order_delivery_neigbhourhood = models.CharField(max_length=100, null=True, blank=True)
