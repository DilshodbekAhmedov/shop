# Generated by Django 4.2 on 2023-04-09 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'verbose_name': 'Maxsulotlar_krimi', 'verbose_name_plural': 'Maxsulotlar_krimlari'},
        ),
        migrations.AlterModelOptions(
            name='incomeitem',
            options={'verbose_name': 'Maxsulot_krimi', 'verbose_name_plural': 'Maxsulot_krimlari'},
        ),
    ]
