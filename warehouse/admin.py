from django.contrib import admin
from .models import Warehouse, WarehouseProduct, Movement, MovementItem

admin.site.register([Warehouse, WarehouseProduct, Movement, MovementItem])
