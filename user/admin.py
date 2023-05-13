from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = 'email', 'first_name', 'user_type', 'is_superuser',
    filter_horizontal = 'user_permissions',
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'avatar', 'email', 'otp', 'user_type', 'birthday', 'phone')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login',)}),
    )
    user_fieldsets = (
        (None, {'fields': ('username', 'password', 'phone')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'email', 'user_type', 'birthday')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff'),
        }),
    )
