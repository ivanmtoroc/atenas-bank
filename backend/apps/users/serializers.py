# Django
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

# Django Rest Framework
from rest_framework import serializers

# Models
from backend.apps.users.models import User

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
