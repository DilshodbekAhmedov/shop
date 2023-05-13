from django.db import models


class Order(models.Model):
    ORDER_STATUS = (
        ("created", "Yaratilgan"),
        ("accepted", "Tasdiqlangan"),
        ("completed", "Tugallangan"),
        ("canceled", 'Rad etilgan'),
    )

    client = models.ForeignKey("client.Client", verbose_name="Xaridor", on_delete=models.PROTECT)
    warehouse = models.ForeignKey('warehouse.Warehouse', verbose_name="Baza", on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(verbose_name="Yaratilgan vaqti", auto_now_add=True)
    status = models.CharField(verbose_name="Maxsulot Xolati", max_length=255, choices=ORDER_STATUS)
    total = models.DecimalField(verbose_name="Narxi", max_digits=17, decimal_places=2, null=True)

    def __str__(self):
        return self.created_at.strftime("%d-%m-%Y")

    class Meta:
        verbose_name = "Zakaz"
        verbose_name_plural = "Zakazlar"


class OrderItem(models.Model):
    order = models.ForeignKey("Order", verbose_name="Zakaz", on_delete=models.PROTECT)
    warehouse_product = models.ForeignKey("warehouse.WarehouseProduct", verbose_name="Maxsulot", on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name="Narxi", max_digits=17, decimal_places=2)
    count = models.IntegerField(verbose_name="Soni")
    total = models.DecimalField(verbose_name="Summasi", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.warehouse_product.product.name

    class Meta:
        verbose_name = "Zakaz birligi"
        verbose_name_plural = "Zakaz birliklari"

