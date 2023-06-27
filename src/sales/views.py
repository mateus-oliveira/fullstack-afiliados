import datetime

from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import SalesTransaction, Seller
from .serializers import SalesTransactionSerializer, SellerSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsAuthenticated]


class SalesTransactionViewSet(viewsets.ModelViewSet):
    queryset = SalesTransaction.objects.all()
    serializer_class = SalesTransactionSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['seller']

    def list(self, request, *args, **kwargs):
        response = super(SalesTransactionViewSet, self).list(request, *args, **kwargs)
        queryset = self.filter_queryset(self.get_queryset())
        response.data['total'] = queryset.aggregate(total=Sum('price'))['total']
        return response

    def create(self, request, *args, **kwargs):
        """ That waits a file with sales information to save the content on database """
        file = request.FILES.get('file')

        if not file:
            return Response({'error': 'File not provided'}, status=status.HTTP_400_BAD_REQUEST)

        success_items = []
        error_items = []

        transactions_to_create = []

        for i, bline in enumerate(file):
            try:
                line = bline.decode()

                # Retrieving information from file
                sale_type = int(line[0])
                purchased_date_str = line[1:26].strip()
                product = line[26:56].strip()
                price = int(line[56:66])
                seller_name = line[66::].strip()

                # Datetime convert
                purchased_date = datetime.datetime.strptime(purchased_date_str, '%Y-%m-%dT%H:%M:%S%z')

                # Seller (Creator or Affiliate)
                seller_type = 2 if (sale_type == 2 or sale_type == 3) else 1
                seller, _ = Seller.objects.get_or_create(name=seller_name, seller_type=seller_type)

                # Sales transaction
                transaction = SalesTransaction(
                    seller=seller,
                    product=product,
                    price=-price if sale_type == 3 else price,
                    purchased_date=purchased_date,
                    sale_type=sale_type
                )
                transactions_to_create.append(transaction)

                success_items.append({'line': f'{i+1} - {line}', 'message': 'Processed successfully'})

            except Exception as e:
                error_items.append({'line':  f'{i+1} - {line}', 'message': str(e)})

        # Bulk creating Sales Transaction
        SalesTransaction.objects.bulk_create(transactions_to_create)

        response_data = {'success_items': success_items, 'error_items': error_items}

        return Response(response_data, status=status.HTTP_200_OK)