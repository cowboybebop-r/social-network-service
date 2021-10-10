from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Test API",
        default_version='v1',
        description="Starnavi Test API documentation",
        contact=openapi.Contact(email="javokhiror@gmail.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
