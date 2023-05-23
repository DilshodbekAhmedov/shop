from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Character, ProductCharacter, ProductMedia, Product, ProductPrice, Country, Manufactory, Category
from . import serializers


class CharacterViewSet(ModelViewSet):
    serializer_class = serializers.CharacterSerializers
    queryset = Character.objects.all()


class CountryViewSet(ModelViewSet):
    serializer_class = serializers.CountrySerializers
    queryset = Country.objects.all()


class ManufactoryViewSet(ModelViewSet):
    serializer_class = serializers.ManufactorySerializers
    queryset = Manufactory.objects.all()


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializers


class ProductMediaViewSet(ModelViewSet):
    serializer_class = serializers.ProductMediaSerializers
    queryset = ProductMedia.objects.all()


class ProductCharactoryViewSet(ModelViewSet):
    serializer_class = serializers.ProductCharactorySerializers
    queryset = ProductCharacter.objects.all()


class ProductPriceViewSet(ModelViewSet):
    serializer_class = serializers.ProductPriceSerializers
    queryset = ProductPrice.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = serializers.CategorySerializers
    queryset = Category.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['slug'] = "-".join(request.data['name'].lower().split())
        response = super().create(request, *args, **kwargs)
        return response
