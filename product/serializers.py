from .models import Country, Manufactory, Category, Product, Character, ProductMedia, ProductCharacter, ProductPrice
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class CountrySerializers(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ManufactorySerializers(ModelSerializer):
    country_obj = CountrySerializers(source="country", many=False, read_only=True)

    class Meta:
        model = Manufactory
        fields = 'id', 'name', 'description', 'country', 'country_obj'


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductMediaSerializers(ModelSerializer):

    class Meta:
        model = ProductMedia
        fields = '__all__'


class CharacterSerializers(ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class ProductCharactorySerializers(ModelSerializer):
    character_obj = CharacterSerializers(source='character', many=False, read_only=True)

    class Meta:
        model = ProductCharacter
        fields = '__all__'


class ProductPriceSerializers(ModelSerializer):

    class Meta:
        model = ProductPrice
        fields = '__all__'


class ProductSerializers(ModelSerializer):
    category_obj = CategorySerializers(source='category', many=False, read_only=True)
    manufactory_obj = ManufactorySerializers(source='manufactory', many=False, read_only=True)
    country_obj = CountrySerializers(source='country', many=False, read_only=True)
    product_media_obj = ProductMediaSerializers(source='product_media', many=True, read_only=True)
    product_character_obj = ProductCharactorySerializers(source='product_character', many=True, read_only=True)
    product_price_obj = CountrySerializers(source='product_price', many=True, read_only=True)

    class Meta:
        model = Product
        fields = 'id', 'name', 'sale_count', 'view_count', 'is_active', 'category', \
            'manufactory', 'country', 'category_obj', 'manufactory_obj', 'country_obj', \
            'product_media_obj', 'product_character_obj', 'product_price_obj'




