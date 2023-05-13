import decimal
from _decimal import Decimal
from .income_update import add_all_total
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from income.models import Income, IncomeItem
from warehouse.models import Warehouse, WarehouseProduct
from .serializers import IncomeSerializer, IncomeItemSerializer
from rest_framework.response import Response
from rest_framework import status
from warehouse.models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from provider.models import Provider


class StatusFilter(filters.FilterSet):
    status = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Income
        fields = ('status',)


class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    filterset_class = StatusFilter

    @action(detail=True, methods=['post'])
    def move_income(self, request, *args, **kwargs):
        obj_income = self.get_object()
        provider_obj = obj_income.provider
        obj_income_items = IncomeItem.objects.filter(income=obj_income.id)
        if obj_income.status == 'created':
            obj_income.status = 'accepted'
        elif obj_income.status == 'canceled':
            obj_income.status = 'created'
        elif obj_income.status == 'accepted':
            obj_income.status = 'completed'
            provider_obj.balance += obj_income.total
            provider_obj.save()
            for i in obj_income_items:
                wp_obj, created = WarehouseProduct.objects.get_or_create(
                    warehouse=obj_income.warehouse,
                    product=i.product,
                    defaults={
                        'count': i.count,
                        'self_price': i.price,
                        'total': i.price * i.count
                    }
                )
                if not created:
                    wp_obj.count += i.count
                    wp_obj.total += i.total
                    wp_obj.self_price = wp_obj.total / wp_obj.count
                    wp_obj.save()
        obj_income.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['post'])
    def cancel_income(self, request, *args, **kwargs):
        obj_income = self.get_object()
        obj_provider = obj_income.provider
        if obj_income.status == 'completed':
            obj_income_items = IncomeItem.objects.filter(income=obj_income)
            obj_provider.balance -= obj_income.total
            obj_provider.save()
            for income_item in obj_income_items:
                wp_obj = WarehouseProduct.objects.get(product=income_item.product, warehouse=obj_income.warehouse)
                wp_obj.count -= income_item.count
                wp_obj.save()
        obj_income.status = 'canceled'
        obj_income.save()
        return Response("Status changed")


class IncomeItemViewSet(ModelViewSet):
    queryset = IncomeItem.objects.all()
    serializer_class = IncomeItemSerializer

    def create(self, request, *args, **kwargs):
        total = Decimal(request.data['price']) * Decimal(request.data['count'])
        request.data['total'] = total
        response = super().create(request, *args, **kwargs)
        income_obj = Income.objects.get(id=request.data['income'])
        income_obj.save()
        add_all_total(income_obj.id)
        return response

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        income_obj = instance.income
        instance.total = instance.price * Decimal(instance.count)
        instance.save()
        response = super().update(request, *args, **kwargs)
        add_all_total(income_obj.id)
        return response

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = kwargs.get("many", True)
        return super(IncomeItemViewSet, self).get_serializer(*args, **kwargs)




