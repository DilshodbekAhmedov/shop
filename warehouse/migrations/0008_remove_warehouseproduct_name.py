# Generated by Django 4.2 on 2023-05-04 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_warehouseproduct_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouseproduct',
            name='name',
        ),
    ]