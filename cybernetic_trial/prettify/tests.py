from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class Test(TestCase):
    def test_non_number_input(self):
        url = reverse('prettify')
        input_num = {'input_number': 'sdflk'}
        response = self.client.post(url, data=input_num)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a number.')

    def test_too_long_num(self):
        url = reverse('prettify')
        long_num = str(pow(10, 1000))
        input_num = {'input_number': long_num}
        response = self.client.post(url, data=input_num)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Number is too long.')

    def test_float_num(self):
        url = reverse('prettify')
        input_num = {'input_number': '23423.34534'}
        response = self.client.post(url, data=input_num)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '23.4k')
