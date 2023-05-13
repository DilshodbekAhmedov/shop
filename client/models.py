from django.db import models


class Client(models.Model):
    full_name = models.CharField(verbose_name="Xaridorning to'liq ishm familiyasi", max_length=255)
    phone = models.CharField(verbose_name="Telefon raqam", max_length=13)
    balance = models.DecimalField(verbose_name="Balansi", max_digits=17, decimal_places=2)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Xaridor"
        verbose_name_plural = "Xaridorlar"
