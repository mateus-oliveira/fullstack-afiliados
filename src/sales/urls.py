from django.urls import path, include
from rest_framework import routers
from .views import SalesTransactionViewSet, AuthViewSet

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for your project",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register('sales-transactions', SalesTransactionViewSet, basename='sales-transactions')

urlpatterns = [
    path('login/', AuthViewSet.as_view(), name='login'),
    path("", include((router.urls, 'sales'), namespace='sales')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
