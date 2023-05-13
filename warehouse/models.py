from django.db import models
from product.models import Product

class Warehouse(models.Model):
    name = models.CharField(verbose_name="Baza nomi", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Baza"
        verbose_name_plural = "Bazalar"


class WarehouseProduct(models.Model):
    warehouse = models.ForeignKey("Warehouse", verbose_name="Baza", on_delete=models.PROTECT)
    product = models.ForeignKey("product.Product", verbose_name="Maxsulot nomi", on_delete=models.PROTECT)
    count = models.IntegerField(verbose_name="Soni")
    total = models.DecimalField(verbose_name="Summasi", max_digits=17, decimal_places=2, null=True)
    self_price = models.DecimalField(verbose_name="Maxsulotning tan narxi", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Bazadagi maxsulot"
        verbose_name_plural = "Bazadagi maxsulotlar"


class Movement(models.Model):
    MOVEMENT_STATUS = (
        ("created", "Yaratilgan"),
        ("accepted", "Tasdiqlangan"),
        ("completed", "Tugallangan"),
        ("canceled", 'Rad etilgan'),
    )
    from_warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT,
                                       related_name="from_warehouse", verbose_name="Bazadan")
    to_warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT,
                                     related_name="to_warehouse", verbose_name="Bazaga")
    status = models.CharField(verbose_name="Statusi", max_length=255, choices=MOVEMENT_STATUS, null=True)


class MovementItem(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.PROTECT, verbose_name="Ko'chirma")
    warehouse_product = models.ForeignKey(WarehouseProduct, on_delete=models.PROTECT, verbose_name="Maxsulot")
    count = models.IntegerField(verbose_name="Maxsulot soni")





