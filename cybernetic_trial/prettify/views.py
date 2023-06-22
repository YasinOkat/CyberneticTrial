from django.shortcuts import render


# Create your views here.

def prettify(request):
    if request.method == 'POST':
        input_number = float(request.POST.get('input_number', 0))

        return render(request, 'prettify.html', {'output_number': prettify_num(input_number)})
    else:
        return render(request, 'prettify.html')


def prettify_num(num):
    num_length = len(str(int(num)))

    if 3 < num_length < 5:
        truncated = round((num / pow(10, 3)), 1)
        prettified = int(truncated) if truncated.is_integer() else truncated
        return str(prettified) + 'k'
    elif 9 > num_length > 6:
        truncated = round((num / pow(10, 6)), 1)
        prettified = int(truncated) if truncated.is_integer() else truncated
        return str(prettified) + 'M'
    elif num_length > 9:
        truncated = round((num / pow(10, 9)), 1)
        prettified = int(truncated) if truncated.is_integer() else truncated
        return str(prettified) + 'B'
    else:
        return str(int(num))
