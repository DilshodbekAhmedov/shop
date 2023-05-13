from _decimal import Decimal
from .order_update import add_all_total
from warehouse.models import WarehouseProduct
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from django_filters import rest_framework as filters
from rest_framework.response import Response


class StatusClientFilter(filters.FilterSet):
    status = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ('status', 'client')


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = StatusClientFilter

    @action(detail=True, methods=['post'])
    def status_change(self, request, *args, **kwargs):
        obj_order = self.get_object()
        obj_client = obj_order.client
        if obj_order.status == 'created':
            obj_order.status = 'accepted'
        elif obj_order.status == 'canceled':
            obj_order.status = 'created'
        elif obj_order.status == 'accepted':
            obj_client.balance += obj_order.total
            obj_client.save()
            obj_order_items = OrderItem.objects.filter(order=obj_order.id)
            for order_item in obj_order_items:
                wp_obj = order_item.warehouse_product
                wp_obj.count -= order_item.count
                wp_obj.save()
            obj_order.status = 'completed'
        obj_order.save()
        return Response("Status changed")

    @action(detail=True, methods=['post'])
    def cancel_order(self, request, *args, **kwargs):
        order_obj = self.get_object()

        order_items_obj = OrderItem.objects.filter(order=order_obj)
        if order_obj.status == "completed":
            client_obj = order_obj.client
            client_obj.balance += order_obj.total
            client_obj.save()
            for order_item in order_items_obj:
                wp_obj = order_item.warehouse_product
                wp_obj.count += order_item.count
                wp_obj.save()
        order_obj.status = 'canceled'
        order_obj.save()
        return Response("Status changed")



class OrderItemFilter(filters.FilterSet):
    status = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = OrderItem
        fields = ('order',)


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filterset_class = OrderItemFilter

    def create(self, request, *args, **kwargs):
        request.data['total'] = float(request.data['price']) * float(request.data['count'])
        response = super().create(request, *args, **kwargs)
        order_obj = Order.objects.get(id=request.data['order'])
        order_obj.save()
        add_all_total(order_obj.id)
        return response

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        order_obj = instance.order
        instance.total = instance.price * Decimal(instance.count)
        instance.save()
        response = super().update(request, *args, **kwargs)
        add_all_total(order_obj.id)
        return response

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = kwargs.get("many", True)
        return super(OrderItemViewSet, self).get_serializer(*args, **kwargs)
