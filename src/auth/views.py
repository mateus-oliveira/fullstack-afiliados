from rest_framework_simplejwt.views import TokenViewBase
from .serializers import AuthSerializer


class AuthViewSet(TokenViewBase):
    serializer_class = AuthSerializer