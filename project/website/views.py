from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Page


# Create your views here.
def index(request):
    return render(request, 'base.html')


def get_help(request):
    return render(request, 'get_help.html')


def volunteer(request):
    return render(request, 'volunteer.html')


def get_page(request, slug):
    page = get_object_or_404(
        Page.objects.filter(published=True),
        slug=slug
    )
    return render(request, 'page.html', {
        'page': page
    })
