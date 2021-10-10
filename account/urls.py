from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegistrationAPIView, UserDeviceLoginView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('login/', UserDeviceLoginView.as_view(), name='login-view'),
]
