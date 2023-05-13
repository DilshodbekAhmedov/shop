import base64
import io
from django.core.files import File
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import User
from rest_framework.validators import UniqueValidator


def password_validator(value):
    if len(value) < 8:
        raise ValidationError("This is bad password")
    else:
        return True


class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=(password_validator, ),
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('password',)


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def forget_password(self, instance, validated_data):
        email = validated_data['email']

        print(email)


class CheckUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=(password_validator, ),
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    avatar = serializers.CharField(required=False)

    def create(self, validated_data):
        password = self.initial_data.get('password', False)
        avatar = self.initial_data.get('avatar', False)
        if not password:
            raise ValueError('error')
        if self.initial_data.get('avatar', False):
            validated_data.pop('avatar')
        instance = super().create(validated_data)
        instance.password = make_password(password)
        if avatar:
            p = base64.b64decode(self.initial_data.get('avatar', False))
            img = io.BytesIO()
            img.write(p)
            instance.avatar = File(name=f"avatar_{instance.id}", file=img)
        instance.is_active = False
        instance.save()
        return instance

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'avatar', 'email', 'username', 'is_active', 'birthday', 'phone', \
            'user_type',


class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
