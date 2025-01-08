from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')


def second_page(request):
    return render(request, 'second_page.html')


def third_page(request):
    return render(request, 'third_page')
