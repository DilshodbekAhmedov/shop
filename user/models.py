from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.dispatch import receiver
from django_resized import ResizedImageField

from user.validators import phone_validator


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def _create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.

        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('director', 'Director'),
        ('admin', 'Admin'),
        ('seller', 'Soruvchi')
    )
    first_name = models.CharField(verbose_name='Ism', max_length=255, blank=True)
    last_name = models.CharField(verbose_name='Familiya', max_length=255, blank=True)
    avatar = ResizedImageField(verbose_name='Rasim',
                               size=[400, 400],
                               crop=['middle', 'center'],
                               null=True, blank=True,
                               upload_to='user_avatars/')
    email = models.EmailField(verbose_name='Pochta', unique=True)
    otp = models.CharField(max_length=4, null=True, blank=True)
    forget_password_token = models.CharField(max_length=200, null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    username = models.CharField(verbose_name='username', max_length=255, unique=True, blank=True, null=True)
    is_staff = models.BooleanField(verbose_name='Xodimlarning holati', default=False, )
    is_active = models.BooleanField(verbose_name='Faol', default=True, )
    birthday = models.DateField(verbose_name="Tug'ilgan kun",
                                null=True, blank=True)
    phone = models.CharField(verbose_name='Telefon raqami', max_length=255, null=True, blank=False, validators=[phone_validator,])
    user_type = models.CharField(verbose_name='Foydalanuvchi turi', max_length=255, choices=USER_TYPE, default='seller')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'


class ForgetPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


