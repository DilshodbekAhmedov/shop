# Generated by Django 4.2 on 2023-06-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_outlay_outlay_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttransaction',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Naqd pul'), ('card', 'Kartadan'), ('bank', 'Bank')], max_length=255, verbose_name="To'lov usuli"),
        ),
    ]