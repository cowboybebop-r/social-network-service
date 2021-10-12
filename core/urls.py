from django.contrib import admin
from django.urls import path, include

from core.swagger_scheme import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/post/', include('post.urls')),
    path('api/v1/user/', include('account.urls')),
    # path('api/v1/changelog/', include('changelog.urls')),
]

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
