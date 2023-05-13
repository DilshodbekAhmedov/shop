from rest_framework import serializers

from product.models import Product
from .models import Warehouse, WarehouseProduct, Movement, MovementItem


class WarehouseParentProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "name", "full_name", "price", "category"


class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = "__all__"


class WarehouseProductSerializer(serializers.ModelSerializer):
    product_obj = WarehouseParentProductSerializer(source="product", many=False, read_only=True)

    class Meta:
        model = WarehouseProduct
        fields = "__all__"


class MovementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movement
        fields = "__all__"


class MovementItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovementItem
        fields = "__all__"