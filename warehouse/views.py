from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from .models import WarehouseProduct
from .serializers import WarehouseProductSerializer
from django_filters import rest_framework as filters


class WarehouseProductFilter(filters.FilterSet):
    category = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = WarehouseProduct
        fields = ('product',)


class WarehouseProductViewSet(ModelViewSet):
    queryset = WarehouseProduct.objects.all()
    serializer_class = WarehouseProductSerializer
    filterset_class = WarehouseProductFilter



