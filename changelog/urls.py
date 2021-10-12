from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('requestlog', views.RequestLogView, basename='requestlog-api')

urlpatterns = router.urls
