from django.contrib import admin
from .models import Income, IncomeItem

admin.site.register([Income, IncomeItem])

