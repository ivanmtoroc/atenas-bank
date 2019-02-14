# Django Rest Framework
from rest_framework.response import Response
from rest_framework import viewsets

# Serializers
from apps.users.serializers import UserSerializer

# Models
from apps.users.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = not user.is_active
        user.save()
        data = {
            'message': 'Delete success.'
        }
        return Response(data = data)
