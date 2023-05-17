# Generated by Django 4.2 on 2023-05-16 05:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productprice_unit_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprice',
            name='unit_name',
            field=models.UUIDField(default=uuid.UUID('3dc6ec33-a78d-442c-b35c-2a5094b5c45d'), unique=True, verbose_name='Takrorlanmas_id'),
        ),
    ]