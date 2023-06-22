from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


# Create your tests here.
class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test_non_number_input(self):
        response = self.client.get('/abc/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'error': 'Please enter a number.'})

    def test_too_long_num(self):
        long_num = str(pow(10, 1000))
        response = self.client.get('/' + long_num + '/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'error': 'Number is too long.'})

    def test_decimal_num(self):
        input_num = '23423.34534'
        response = self.client.get(f'/{input_num}/', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'prettified_number': '23.4k'})

    def test_million(self):
        input_num = '1000000'
        response = self.client.get(f'/{input_num}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'prettified_number': '1M'})

    def test_billion(self):
        input_num = '3453445453.3423'
        response = self.client.get(f'/{input_num}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'prettified_number': '3.5B'})

    def test_trillion(self):
        input_num = '3453444555453.3423'
        response = self.client.get(f'/{input_num}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"prettified_number": "3.5T"})
