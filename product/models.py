from django.db import models
from uuid import uuid4


class Country(models.Model):
    name = models.CharField(max_length=264, verbose_name='Nomi')

    class Meta:
        verbose_name = 'Davlat'
        verbose_name_plural = 'Davlatlar'

    def __str__(self):
        return self.name


class Manufactory(models.Model):
    name = models.CharField(max_length=264, verbose_name='Nomi')
    description = models.TextField(verbose_name='Haqida')
    country = models.ForeignKey('Country', on_delete=models.PROTECT,
                                verbose_name='Ishlab chiqligan')

    class Meta:
        verbose_name = 'Ishlab Chiqqan Zavod'
        verbose_name_plural = 'Ishlab Chiqqan Zavodlar'

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ForeignKey('Category',
                               verbose_name="Ota kategoriya", on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=264, verbose_name='Nomi')
    slug = models.SlugField(max_length=255)
    photo = models.FileField(verbose_name="Categoriya rasimi",
                             upload_to="product/category_images", null=True, blank=True)

    class Meta:
        verbose_name = 'Categoriya'
        verbose_name_plural = 'Categoriyalar'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')
    category = models.ForeignKey("Category", on_delete=models.PROTECT,
                                 verbose_name='Kategoriya')
    manufactory = models.ForeignKey('Manufactory', on_delete=models.PROTECT,
                                    related_name='manufactory_re',
                                    verbose_name='Ishlab chiqqan Korxona', null=True)  # verbose_name
    country = models.ForeignKey('Country', on_delete=models.PROTECT,
                                verbose_name='Ishlab chiqligan davlat', null=True, blank=True)
    sale_count = models.IntegerField(default=0, verbose_name='Sotilganlar soni')
    view_count = models.PositiveBigIntegerField(default=0,
                                                verbose_name='Ko\'rganlar soni')
    is_active = models.BooleanField(default=True,
                                    verbose_name='Holati Aktiv')

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=264, verbose_name='Nomi')

    class Meta:
        verbose_name_plural = 'Xil(xususiyat)'

    def __str__(self):
        return self.name


class ProductMedia(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT,
                                verbose_name='Mahsulot', related_name='product_media')
    media = models.FileField(upload_to='product/product_images', verbose_name='Video/Rasm', null=True, blank=False)
    is_active = models.BooleanField(default=True, verbose_name='Holati Aktiv')

    class Meta:
        verbose_name_plural = 'Mahsulot Video/rasmlari'

    def __str__(self):
        return self.product.name


class ProductCharacter(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                verbose_name='Mahsulot', related_name='product_character')
    character = models.ForeignKey('Character', on_delete=models.PROTECT, verbose_name='Mahsulot xususiyati')
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Mahsulot xususiyati'

    def __str__(self):
        return self.product.name


class ProductPrice(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                verbose_name='Mahsulot', related_name='product_price')
    unit_type = models.CharField(verbose_name="O'lchov birligi", max_length=255)
    price = models.DecimalField(max_digits=17, decimal_places=2, default=0, verbose_name='Narxi')
    is_active = models.BooleanField(default=True, verbose_name='Holati Aktiv')

    class Meta:
        verbose_name_plural = 'Mahsulot Narxlari'

    def __str__(self):
        return self.product.name