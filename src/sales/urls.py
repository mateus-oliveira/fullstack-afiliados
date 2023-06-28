from django.urls import path, include
from rest_framework import routers
from .views import SalesTransactionViewSet, SellerViewSet


router = routers.DefaultRouter()
router.register('sales-transactions', SalesTransactionViewSet, basename='sales-transactions')
router.register('sellers', SellerViewSet, basename='sellers')

urlpatterns = [
    path("", include((router.urls, 'sales'), namespace='sales')),
]
