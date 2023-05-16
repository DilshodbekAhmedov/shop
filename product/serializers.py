from .models import Country, Manufactory, Category, Product, Character, ProductMedia, ProductCharacter, ProductPrice
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class CountrySerializers(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ManufactorySerializers(ModelSerializer):
    country = CountrySerializers(read_only=True)

    class Meta:
        model = Manufactory
        fields = '__all__'


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductMediaSerializers(ModelSerializer):
    product = serializers.StringRelatedField(source='product_media', read_only=True)

    class Meta:
        model = ProductMedia
        fields = '__all__'


class CharactorySerializers(ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class ProductCharactorySerializers(ModelSerializer):
    product = serializers.StringRelatedField(source='product_character', read_only=True)

    class Meta:
        model = ProductCharacter
        fields = '__all__'


class ProductPriceSerializers(ModelSerializer):
    product = serializers.StringRelatedField(source='product_price', read_only=True)

    class Meta:
        model = ProductPrice
        fields = '__all__'


class ProductSerializers(ModelSerializer):
    country = CountrySerializers(read_only=True)
    category = CategorySerializers(read_only=True)
    manufactory = ManufactorySerializers(read_only=True)
    product_media = ProductMediaSerializers(many=True, read_only=True)
    product_charactory = ProductCharactorySerializers(many=True, read_only=True)
    product_price = ProductPriceSerializers(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'manufactory', 'country', 'sale_count', 'view_count', 'product_media',
                  'product_charactory',
                  'is_active', 'product_price']
