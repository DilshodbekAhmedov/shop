from rest_framework import serializers

from product.models import Product
from warehouse.models import WarehouseProduct
from .models import Order, OrderItem


class OrderChildProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ChildWarehouseProductSerializer(serializers.ModelSerializer):
    product_obj = OrderChildProductSerializer(source='product', many=False, read_only=True)

    class Meta:
        model = WarehouseProduct
        fields = "warehouse", "product", "count", "total", "self_price", "product_obj",


class ChildOrderItemSerializer(serializers.ModelSerializer):
    warehouse_product_obj = ChildWarehouseProductSerializer(source='warehouse_product', many=False, read_only=True)

    class Meta:
        model = OrderItem
        fields = "warehouse_product", "price", "count", "total",  "warehouse_product_obj",


class OrderSerializer(serializers.ModelSerializer):
    order_items = ChildOrderItemSerializer(source='orderitem_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"
