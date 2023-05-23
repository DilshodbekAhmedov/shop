# Generated by Django 4.2 on 2023-05-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_user_is_verified_alter_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('super_admin', 'Super Admin'), ('admin', 'Admin'), ('seller', 'Soruvchi'), ('client', 'Xaridor')], default='client', max_length=255, verbose_name='Foydalanuvchi turi'),
        ),
    ]
