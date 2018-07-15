from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from app.forms import BrandForm, ItemForm, CategoryForm

# Create your views here.
def create_brand(request, username=None):
    return render(request, 'brand.html', {})

def create_item(request):
    return render(request, 'item.html', {})

def index(request):

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = BrandForm()

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    category_form = CategoryForm()

    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            item_form.save()
            return HttpResponseRedirect('/')
    item_form = ItemForm()

    return render(request, 'index.html', {
        'form': form,
        'item_form': item_form,
        'category_form': category_form
    })
