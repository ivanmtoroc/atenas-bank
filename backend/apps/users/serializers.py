# Django
from django.contrib.auth import password_validation, authenticate
from django.core.exceptions import ValidationError

# Django Rest Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Models
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    passwd = serializers.CharField(source = 'password')
    passwd_confirmation = serializers.CharField(source = 'password')

    class Meta:
        model = User
        fields = (
            'username',
            'identification',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'phone',
            'address',
            'position',
            'passwd',
            'passwd_confirmation'
        )
        extra_kwargs = {
            'passwd': { 'write_only': True },
            'passwd_confirmation': { 'write_only': True }
        }

    def validate_passwd(self, value):
        data = self.get_initial()
        passwd_confirmation = data.get('passwd_confirmation')
        if value != passwd_confirmation:
            raise ValidationError("Password dont match.")
        password_validation.validate_password(value)
        return value

    def create(self, data):
        user = User.objects.create_user(**data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 20)
    passwd = serializers.CharField(min_length = 8, max_length = 64)

    def validate(self, data):
        user = authenticate(username = data['username'], password = data['passwd'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user = self.context['user'])
        return self.context['user'], token.key
