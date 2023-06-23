from rest_framework import serializers
from .models import SalesTransaction, Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class SalesTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTransaction
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['seller'] = SellerSerializer()
        return super(SalesTransactionSerializer, self).to_representation(instance)