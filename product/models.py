from django.db import models


class Category(models.Model):
    parent = models.ForeignKey("Category", verbose_name="Otasi", on_delete=models.CASCADE,
                               null=True, blank=True, related_name="childes")
    name = models.CharField(verbose_name="Nomi", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoriya"
        verbose_name_plural = "Categiriyalar"


class Product(models.Model):
    category = models.ForeignKey("Category", verbose_name="Kategoriyasi",
                                 on_delete=models.PROTECT, related_name="products")
    name = models.CharField(verbose_name="Nomi", max_length=255)
    full_name = models.CharField(max_length=255, verbose_name="To'liq nomi", null=True)
    price = models.DecimalField(verbose_name="Narxi", max_digits=17, decimal_places=2, null=True)
    description = models.TextField(verbose_name="Masulot haqida ma'lumot")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"
