from django.contrib.auth.models import update_last_login
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenViewBase

from .models import User
from .serializers import RegistrationSerializer, CustomTokenObtainPairSerializer, UserLogSerializer


class RegistrationView(GenericViewSet, CreateModelMixin):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        return super(RegistrationView, self).create(request, *args, **kwargs)


class LoginView(TokenViewBase):
    """
    Token View with custom token serializer
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = CustomTokenObtainPairSerializer

    www_authenticate_realm = 'api'

    def get_authenticate_header(self, request):
        return '{0} realm="{1}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm,
        )

    def post(self, request, *args, **kwargs):
        result = super(LoginView, self).post(request, *args, **kwargs)
        try:
            user = User.objects.get(id=result.data['user_id'])
            update_last_login(None, user)
        except Exception as ex:
            return print(ex)
        return result


class UserLogView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserLogSerializer

    def list(self, request, *args, **kwargs):
        return super(UserLogView, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(UserLogView, self).retrieve(request, *args, **kwargs)
