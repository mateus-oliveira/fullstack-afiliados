from django.urls import path, include
from rest_framework import routers
from .views import SalesTransactionViewSet, AuthViewSet

router = routers.DefaultRouter()
router.register('sales-transactions', SalesTransactionViewSet, basename='sales-transactions')

urlpatterns = [
    path('login/', AuthViewSet.as_view(), name='login'),
    path("", include((router.urls, 'sales'), namespace='sales')),
]
