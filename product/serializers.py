import base64
import io
from django.core.files import File
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


class ChildCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ChildProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    child_categories = ChildCategorySerializer(source='category_set', many=True, read_only=True)

    # products_obj = ChildProductSerializer(source='product_set', many=True, read_only=True)
    photo = serializers.CharField(required=False)

    def create(self, validated_data):
        photo = self.initial_data.get('photo', False)
        if self.initial_data.get('photo', False):
            validated_data.pop('photo')
        instance = super().create(validated_data)
        if photo:
            format = photo.split('/')[1].split(';')[0]
            if format == "svg+xml":
                format = "svg"
            photo = photo.split(',')[1]
            p = base64.b64decode(photo)
            img = io.BytesIO()
            img.write(p)
            instance.photo = File(name=f"photo_{instance.id}.{format}", file=img)
        instance.save()
        return instance

    class Meta:
        model = Category
        fields = "id", "parent", "name", "slug", "photo", "child_categories",


class ProductMediaSerializers(ModelSerializer):
    media = serializers.CharField(required=False)

    def create(self, validated_data):
        media = self.initial_data.get('media', False)
        if self.initial_data.get('media', False):
            validated_data.pop('media')
        instance = super().create(validated_data)
        if media:
            format = media.split('/')[1].split(';')[0]
            if format == "svg+xml":
                format = "svg"
            media = media.split(',')[1]
            # print(media)
            p = base64.b64decode(media)
            img = io.BytesIO()
            img.write(p)
            instance.media = File(name=f"media_{instance.id}.{format}", file=img)
        instance.save()
        return instance
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
