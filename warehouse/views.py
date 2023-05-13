from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from .models import Warehouse, WarehouseProduct, Movement, MovementItem
from .serializers import WarehouseSerializer, WarehouseProductSerializer, MovementSerializer, MovementItemSerializer
from django_filters import rest_framework as filters


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseProductFilter(filters.FilterSet):
    category = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = WarehouseProduct
        fields = ('warehouse',)


class WarehouseProductViewSet(ModelViewSet):
    queryset = WarehouseProduct.objects.all()
    serializer_class = WarehouseProductSerializer
    filterset_class = WarehouseProductFilter


class MovementViewSet(ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

    @action(detail=True, methods=['post'])
    def move_product(self, request, *args, **kwargs):
        obj_movement = self.get_object()
        if obj_movement.status == 'created':
            obj_movement.status = 'accepted'
        elif obj_movement.status == 'canceled':
            obj_movement.status = 'created'
        elif obj_movement.status == 'accepted':
            obj_movement_items = MovementItem.objects.filter(
                movement=obj_movement.id)
            for obj_mov_item in obj_movement_items:
                wp_obj = obj_mov_item.warehouse_product
                wp_obj.count -= obj_mov_item.count
                wp_to_obj, created = WarehouseProduct.objects.get_or_create(
                    warehouse=obj_movement.to_warehouse,
                    product=obj_mov_item.warehouse_product.product,
                    defaults={
                        'count': obj_mov_item.count,
                        'self_price': wp_obj.self_price,
                        'total': wp_obj.self_price * wp_obj.count
                    }
                )
                if not created:
                    wp_to_obj.count += obj_mov_item.count
                    wp_to_obj.total += wp_obj.count * wp_obj.self_price
                    wp_to_obj.self_price = wp_obj.self_price
                    wp_to_obj.save()

                wp_obj.save()
            obj_movement.status = 'completed'
        obj_movement.save()
        return Response("Status changed")

    @action(detail=True, methods=['post'])
    def cancel_movement(self, request, *args, **kwargs):
        obj_movement = self.get_object()
        if obj_movement.status == 'completed':
            obj_movement_items = MovementItem.objects.filter(movement=obj_movement)
            for movement_item in obj_movement_items:
                wp_obj = WarehouseProduct.objects.get(product=movement_item.warehouse_product.product, warehouse=obj_movement.to_warehouse)
                wp_obj.count -= movement_item.count
                wp_obj.save()
                from_wp_item = movement_item.warehouse_product
                from_wp_item.count += movement_item.count
                from_wp_item.save()
        obj_movement.status = 'canceled'
        obj_movement.save()
        return Response("Status changed")


class MovementItemViewSet(ModelViewSet):
    queryset = MovementItem.objects.all()
    serializer_class = MovementItemSerializer

