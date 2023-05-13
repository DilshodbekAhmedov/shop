from django.db import models


class OutlayCategory(models.Model):
    name = models.CharField(verbose_name="Xarajotlar kategoriyasi", max_length=255)

    def __str__(self):
        return self.name


class Outlay(models.Model):
    name = models.CharField(verbose_name="Xarajot nomi", max_length=255)
    outlay_category = models.ForeignKey('OutlayCategory', verbose_name="Xarajot kategoriyasi", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class PaymentTransaction(models.Model):
    PAYMENT_MEYHOD = (
        ('cash', "Naqd pul"),
        ('card', "Cartadan"),
        ('bank', 'Bank'),
    )
    PAYMENT_TYPE = (
        ('income', "Tavar krimi"),
        ('order', "Zakaz"),
        ('client', "Xaridor"),
        ('provider', "Yetkazib beruvchi"),
        ('outlay', "Xarajat"),
    )
    TRANSACTION_TYPE = (
        ('income', "Krim"),
        ('outcome', "Chiqim")
    )
    payment_method = models.CharField(verbose_name="To'lov usuli", max_length=255, choices=PAYMENT_MEYHOD)
    payment_type = models.CharField(verbose_name="To'lov turi", max_length=255, choices=PAYMENT_TYPE)
    transaction_type = models.CharField(verbose_name="Tranzaksiya turi", max_length=50, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=17, decimal_places=2, verbose_name="Qiymati")
    is_deleted = models.BooleanField(verbose_name="O'chirilgan")
    comment = models.CharField(verbose_name="Izoh", max_length=400)
    income = models.ForeignKey('income.Income', verbose_name="Maxsulot krimi",
                               on_delete=models.PROTECT, null=True, blank=True)
    order = models.ForeignKey('order.Order', verbose_name="Zakaz", on_delete=models.PROTECT, null=True, blank=True)
    client = models.ForeignKey('client.Client', verbose_name="Xaridor", on_delete=models.PROTECT, null=True, blank=True)
    provider = models.ForeignKey('provider.Provider', verbose_name="Yetkazib beruvchi",
                                 on_delete=models.PROTECT, null=True, blank=True)
    outlay = models.ForeignKey('Outlay', verbose_name="Xarajat nomi", on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    deleted_at = models.DateTimeField(auto_now_add=True, verbose_name="O'chirilgan sana", null=True, blank=True)
    created_user = models.ForeignKey('user.User', verbose_name="Yaratgan xodim",
                                     on_delete=models.PROTECT, related_name='created_user')
    deleted_user = models.ForeignKey('user.User', verbose_name="O'chirgan xodim",
                                     on_delete=models.PROTECT, null=True, blank=True, related_name='deleted_user')