from django.shortcuts import render
from django.http import HttpResponse

from app.forms import BrandForm

# Create your views here.
def create_brand(request, username=None):
    return render(request, 'brand.html', {})

def create_item(request):
    return render(request, 'item.html', {})

def index(request):

    if request == 'POST':
        form = BrandForm()
        if form.is_valid():
            return HttpResponseRedirect('/')

    form = BrandForm()
    return render(request, 'index.html', {'form': form})
