from django.shortcuts import render


# Create your views here.
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
        truncated = round((num / pow(10, 3)), 1)
        prettified = int(truncated) if truncated.is_integer() else truncated
        return str(prettified) + 'k'
    elif 9 >= num_length > 6:
        truncated = round((num / pow(10, 6)), 1)
        prettified = int(truncated) if truncated.is_integer() else truncated
        return str(prettified) + 'M'
    elif num_length > 9:
        truncated = round((num / pow(10, 9)), 1)
        prettified = int(truncated) if truncated.is_integer() else truncated
        return str(prettified) + 'B'
    else:
        return str(int(num))
