from django.contrib import admin
from .models import MobileProducts,LaptopProducts,SmartWatchProducts,Review

admin.site.register(MobileProducts)

admin.site.register(LaptopProducts)

admin.site.register(SmartWatchProducts)

admin.site.register(Review)