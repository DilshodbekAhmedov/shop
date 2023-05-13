from django.db import models


class Provider(models.Model):
    name = models.CharField(verbose_name="Yitkazib beruvchi", max_length=255)
    phone = models.CharField(max_length=13)
    balance = models.DecimalField(verbose_name="Balansi", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yitkazib beruvchi"
        verbose_name_plural = "Yitkazib beruvchilar"


