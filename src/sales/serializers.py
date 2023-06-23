from rest_framework import serializers
from .models import SalesTransaction


class SalesTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTransaction
        fields = '__all__'