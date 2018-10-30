from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(source = 'password')
    password2 = serializers.CharField(source = 'password')

    class Meta:
        model = User
        fields = (
            'username',
            'cedula',
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
        data = self.get_initial()
        password2 = data.get('password2')
        print(value)
        print(password2)
        if value != password2:
            raise ValidationError("Password does not match.")
        return value

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            cedula = validated_data['cedula'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            phone = validated_data['phone'],
            address = validated_data['address'],
            password = validated_data['password']
        )
        user.set_password(user.password)
        user.save()
        return validated_data
