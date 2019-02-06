# Django
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

# Django Rest Framework
from rest_framework import serializers

# Models
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    password_registration = serializers.CharField(source = 'password')
    password_confirmation = serializers.CharField(source = 'password')

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
            'password_registration',
            'password_confirmation'
        )
        extra_kwargs = {
            'password_registration': { 'write_only': True },
            'password_confirmation': { 'write_only': True }
        }

    def validate_password_registration(self, value):
        data = self.get_initial()
        password_confirmation = data.get('password_confirmation')
        if value != password_confirmation:
            raise ValidationError("Password does not match.")
        password_validation.validate_password(value)
        return value

    def create(self, data):        
        user = User.objects.create_user(**data)
        return user
