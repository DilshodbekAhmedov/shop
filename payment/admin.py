from django.contrib import admin
from .models import PaymentTransaction, OutlayCategory, Outlay

admin.site.register([OutlayCategory, Outlay, PaymentTransaction])
