from django.db import models


class Income(models.Model):
    INCOME_STATUS = (
        ("created", "Yaratilgan"),
        ("accepted", "Tasdiqlangan"),
        ("completed", "Tugallangan"),
        ("canceled", 'Rad etilgan'),
    )
    provider = models.ForeignKey('provider.Provider', verbose_name="Yitkazib beruvchi", on_delete=models.PROTECT)
    warehouse = models.ForeignKey("warehouse.Warehouse", verbose_name="Baza", on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(verbose_name="Yasalgan vaqti", auto_now_add=True)
    status = models.CharField(verbose_name="Statusi", max_length=255, choices=INCOME_STATUS, default="created")
    total = models.DecimalField(verbose_name="Narxi", max_digits=17, decimal_places=2, default=0)

    def __str__(self):
        return self.created_at.strftime("%d-%m-%Y")

    class Meta:
        verbose_name = "Maxsulotlar_krimi"
        verbose_name_plural = "Maxsulotlar_krimlari"


class IncomeItem(models.Model):
    income = models.ForeignKey("Income", verbose_name="Krim", on_delete=models.PROTECT)
    product = models.ForeignKey("product.Product", verbose_name="Maxsulot", on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name="Narxi", max_digits=17, decimal_places=2)
    count = models.IntegerField(verbose_name="Soni")
    total = models.DecimalField(verbose_name="Summasi", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Maxsulot_krimi"
        verbose_name_plural = "Maxsulot_krimlari"
