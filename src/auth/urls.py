from django.urls import path
from .views import AuthViewSet


urlpatterns = [
    path('login/', AuthViewSet.as_view(), name='login'),
]
