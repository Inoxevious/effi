from django.contrib import admin
from . models import Hotspot, ActiveHotspot
from mapwidgets.widgets import GooglePointFieldInlineWidget
from django.contrib.gis.db.models import PointField
class HotspotAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldInlineWidget}
    }
    # fieldsets = [
    #     (None, {'fields': ['reference','qrCode','picture','location','deliveryAddress','unitNumber','package_user','available','valid']}),
    # ]
    list_display = ('manager','reference','city','available')
    list_filter = ('city','available')
# Register your models here.
class ActiveHotspotAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldInlineWidget}
    }
    # fieldsets = [
    #     (None, {'fields': ['reference','qrCode','picture','location','deliveryAddress','unitNumber','package_user','available','valid']}),
    # ]
    list_display = ('hotspot','desiel_pump_price','petrol_pump_price','gas_pump_price')
    list_filter = ('hotspot','desiel_pump')
# Register your models here.



admin.site.register(Hotspot, HotspotAdmin)
admin.site.register(ActiveHotspot, ActiveHotspotAdmin)