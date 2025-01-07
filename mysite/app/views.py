from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

class Index2(TemplateView):
    template_name = 'index2.html'