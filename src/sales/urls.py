from django.urls import path, include
from rest_framework import routers
from .views import SalesTransactionViewSet


router = routers.DefaultRouter()
router.register('sales-transactions', SalesTransactionViewSet, basename='sales-transactions')

urlpatterns = [
    path("", include((router.urls, 'sales'), namespace='sales')),
]
