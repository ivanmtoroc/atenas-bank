# Rest Framework
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

# Users models
from apps.users.models import UserModel

# Users serializers
from apps.users.serializers import UserSerializer, LoginSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    # def get_permissions(self):
    #     if self.action in ['login']:
    #         permissions = [AllowAny]
    #     else:
    #         permissions = [IsAuthenticated,]
    #     return [ p() for p in permissions ]

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = not user.is_active
        user.save()
        data = { 'message': 'Deleted successfully.' }
        return Response(data)

    @action(detail = False, methods = ['post'])
    def login(self, request, pk = None):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user, token = serializer.save()
        user = UserSerializer(user).data
        data = {
            'user': {
                'id': user.get('id'),
                'identification': user.get('identification'),
                'username': user.get('username'),
                'email': user.get('email'),
                'name': '{} {}'.format(user.get('first_name'), user.get('last_name')),
                'position': user.get('position')
            },
            'token': token
        }
        return Response(data)
