import tempfile

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker


class SalesTransactionViewSetTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('sales:sales-transactions-list')
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)

        file_content = (
            b'12022-01-15T19:20:30-03:00CURSO DE BEM-ESTAR\n'
            b'12021-12-03T11:46:02-03:00DOMINANDO INVESTIMENTOS       0000050000JOAO MARIA\n'
            b'12021-12-03T11:46:02-03:00DOMINANDO INVESTIMENTOS       0000050000MARIA CANDIDA'
        )

        self.temp_file.write(file_content)
        self.temp_file.seek(0)

    def test_create_sales_transactions_authenticated(self):
        """ Ensure the view requires authentication """
        response = self.client.post(self.url, {'file': self.temp_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_sales_transactions_with_invalid_file(self):
        """ Ensure an error is returned when an invalid file is provided """
        self.client.force_authenticate(user=baker.make('User'))  # Authenticate the user
        invalid_file_content = "Invalid file content"

        response = self.client.post(self.url, {'file': invalid_file_content}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'File not provided')

    def test_create_sales_transactions_with_empty_file(self):
        """ Ensure an error is returned when an empty file is provided """
        self.client.force_authenticate(user=baker.make('User'))  # Authenticate the user

        response = self.client.post(self.url, {'file': ''}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'File not provided')

    def test_create_sales_transactions_with_missing_fields(self):
        """ Ensure an errors list is returned when the file has missing fields """
        self.client.force_authenticate(user=baker.make('User'))

        response = self.client.post(self.url, {'file': self.temp_file}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data['success_items']), 2)
        self.assertEqual(len(response.data['error_items']), 1)
