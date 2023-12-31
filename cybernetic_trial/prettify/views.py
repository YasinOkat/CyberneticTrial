import requests
from django.shortcuts import render
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response


# This is the REST API
class PrettifyNumber(APIView):
    def get(self, request, input_num):
        try:
            input_num = float(input_num)  # Converts the input number to float
        except (ValueError, TypeError):
            return Response({'error': 'You should enter a number.'}, status=400)  # Raises exception if the input value
            # couldn't be converted to float

        try:
            prettified_number = prettify_num(input_num)  # Calls the function with argument number
        except OverflowError:
            return Response({'error': 'Number is too long to be evaluated.'}, status=400)

        return Response({'prettified_number': prettified_number})  # Returns the prettified number as JSON format


def prettify(request):
    if request.method == 'POST':
        input_number = request.POST.get('input_number', '')  # Get the input number

        try:
            input_number = float(input_number)  # Converts the input number to float
        except ValueError or TypeError:
            return render(request, 'prettify.html', {'error': 'You should enter a number.'})

        try:
            api = reverse('prettify_number', args=[input_number])  # Passes the input number to API
            full_url = request.build_absolute_uri(api)  # Turns it into full URL
            response = requests.get(url=full_url)
            prettified_num = response.json().get('prettified_number')  # Gets the prettified number from API
        except OverflowError:
            return render(request, 'prettify.html', {'error': 'Number is too long to be evaluated.'})

        return render(request, 'prettify.html',
                      {'output_number': prettified_num, 'error': None})  # Renders the page with prettified number
    else:
        return render(request, 'prettify.html')


# The logic to prettify the number:
def prettify_num(num):
    num_length = len(str(int(num)))

    if 3 < num_length <= 6:
        zeroes = 3
        suffix = 'k'
    elif 9 >= num_length > 6:
        zeroes = 6
        suffix = 'M'
    elif 12 >= num_length > 9:
        zeroes = 9
        suffix = 'B'
    elif num_length > 12:
        zeroes = 12
        suffix = 'T'
    else:
        return str(int(num))
    return str(truncate_num(num, zeroes)) + suffix


def truncate_num(num, zeroes):
    truncated = round((num / pow(10, zeroes)), 1)
    prettified = int(truncated) if truncated.is_integer() else truncated
    return prettified
