from django.shortcuts import render


# Create your views here.
def prettify(request):
    return render(request, 'prettify.html')
