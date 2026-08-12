
from tempfile import template
from django.shortcuts import render
def index(request):
    template = "main/index.html"
    return render(request, template)

# Create your views here.
