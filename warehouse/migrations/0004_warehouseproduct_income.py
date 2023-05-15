# Generated by Django 4.2 on 2023-04-13 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0003_income_warehouse'),
        ('warehouse', '0003_warehouseproduct_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouseproduct',
            name='income',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='income.income', verbose_name='Krim'),
        ),
    ]