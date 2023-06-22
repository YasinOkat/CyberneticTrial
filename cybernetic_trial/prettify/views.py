from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class PrettifyNumberView(APIView):
    def get(self, request, number):
        try:
            number = float(number)
        except ValueError or TypeError:
            return Response({'error': 'Please enter a number.'}, status=400)

        try:
            prettified_number = prettify_num(number)
        except OverflowError:
            return Response({'error': 'Number is too long.'}, status=400)

        return Response({'prettified_number': prettified_number})


def prettify(request):
    if request.method == 'POST':
        input_number = request.POST.get('input_number', '')

        try:
            input_number = float(input_number)
        except ValueError or TypeError:
            return render(request, 'prettify.html', {'error': 'Please enter a number.'})

        try:
            prettified_num = prettify_num(input_number)
        except OverflowError:
            return render(request, 'prettify.html', {'error': 'Number is too long.'})

        return render(request, 'prettify.html', {'output_number': prettified_num, 'error': None})
    else:
        return render(request, 'prettify.html')


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

