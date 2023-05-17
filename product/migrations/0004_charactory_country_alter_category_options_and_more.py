# Generated by Django 4.2 on 2023-05-16 04:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_full_name_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charactory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, verbose_name='Nomi')),
            ],
            options={
                'verbose_name_plural': 'Xil(xususiyat)',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, verbose_name='Nomi')),
            ],
            options={
                'verbose_name_plural': 'Davlat',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categoriya'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Mahsulot'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, null=True, verbose_name='Holati Aktiv'),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_count',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=17, null=True, verbose_name='Skidka Narxi'),
        ),
        migrations.AddField(
            model_name='product',
            name='view_count',
            field=models.PositiveBigIntegerField(default=0, null=True, verbose_name="Ko'rganlar soni"),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=264, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category', verbose_name='Kategoriya'),
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.UUIDField(default=uuid.UUID('962dfeae-1cf7-42ae-8d28-174dfe5b8262'), unique=True, verbose_name='Takrorlanmas_id')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Narxi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Holati Aktiv')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productprice', to='product.product', verbose_name='Mahsulot')),
            ],
            options={
                'verbose_name_plural': 'Mahsulot Narxlari',
            },
        ),
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='product/media', verbose_name='Video/Rasm')),
                ('is_active', models.BooleanField(default=True, verbose_name='Holati Aktiv')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productmedia', to='product.product', verbose_name='Mahsulot')),
            ],
            options={
                'verbose_name_plural': 'Mahsulot Video/rasmlari',
            },
        ),
        migrations.CreateModel(
            name='ProductCharactory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('charactory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.charactory', verbose_name='Mahsulot xususiyati')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productcharactory', to='product.product', verbose_name='Mahsulot')),
            ],
            options={
                'verbose_name_plural': 'Mahsulot xususiyati',
            },
        ),
        migrations.CreateModel(
            name='Manufactory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, verbose_name='Nomi')),
                ('description', models.TextField(verbose_name='Haqida')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.country', verbose_name='Ishlab chiqligan')),
            ],
            options={
                'verbose_name_plural': 'Ishlab Chiqqan Zavod',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.country', verbose_name='Ishlab chiqligan davlat'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufactory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='manufactory', to='product.manufactory', verbose_name='Ishlab chiqqan Korxona'),
        ),
    ]