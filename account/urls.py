from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

router = DefaultRouter()

router.register('requestlog', views.UserLogView, basename='requestlog-api')
router.register('registration', views.RegistrationView, basename='registration-api')

urlpatterns = [
    path('token/', views.LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('registration/', views.RegistrationAPIView.as_view(), name='registration'),
]
urlpatterns += router.urls
