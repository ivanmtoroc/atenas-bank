# Django
from django.contrib.auth import password_validation as validators
from django.core.exceptions import ValidationError

# Django Rest Framework
from rest_framework import serializers

# Models
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(source = 'password')
    password2 = serializers.CharField(source = 'password')

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
            'password1',
            'password2'
        )
        extra_kwargs = {
            'password1': { 'write_only': True },
            'password2': { 'write_only': True }
        }

    def validate_password1(self, value):
        validators.validate_password(password = value)
        data = self.get_initial()
        password2 = data.get('password2')
        if value != password2:
            raise ValidationError("Password does not match.")
        return value

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            identification = validated_data['identification'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            position = validated_data['position'],
            phone = validated_data['phone'],
            address = validated_data['address'],
            password = validated_data['password']
        )
        user.set_password(user.password)
        user.save()
        return validated_data
