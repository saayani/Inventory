from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_brand(request, username=None):
    return render(request, 'brand.html', {})

def create_item(request):
    return render(request, 'item.html', {})


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")