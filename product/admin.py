from django.contrib import admin
from .models import *

admin.site.register([Category, Product, Manufactory, ProductMedia, ProductPrice,
                     ProductCharacter, Country, Character   ])

