from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views
from .views import AnalyticView

router = DefaultRouter()

router.register('posts', views.PostCreateRetrieveListView, basename='posts-api')

urlpatterns = [
    url(r'^analytics/$', AnalyticView.as_view(), name='analytics')
]

urlpatterns += router.urls

