from django.db import models
from product.models import Product


class WarehouseProduct(models.Model):
    product = models.ForeignKey("product.Product", verbose_name="Maxsulot nomi", on_delete=models.PROTECT)
    count = models.IntegerField(verbose_name="Soni")
    total = models.DecimalField(verbose_name="Summasi", max_digits=17, decimal_places=2, null=True)
    self_price = models.DecimalField(verbose_name="Maxsulotning tan narxi", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Bazadagi maxsulot"
        verbose_name_plural = "Bazadagi maxsulotlar"









