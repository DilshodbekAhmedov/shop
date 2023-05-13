from rest_framework import serializers
from .models import Category, Product


class ChildCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ChildProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    child_categories = ChildCategorySerializer(source='childes', many=True, read_only=True)
    products = ChildProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "id", "parent", "name", "child_categories", "products",


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
