from rest_framework import serializers

from product.models import Product
from .models import WarehouseProduct


class WarehouseParentProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "id", "name", "category"


class WarehouseProductSerializer(serializers.ModelSerializer):
    product_obj = WarehouseParentProductSerializer(source="product", many=False, read_only=True)

    class Meta:
        model = WarehouseProduct
        fields = "__all__"

