from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'base.html')


def get_help(request):
    return render(request, 'get_help.html')


def volunteer(request):
    return render(request, 'volunteer.html')
