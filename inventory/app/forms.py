from django.forms import ModelForm
from app.models import Brand, Item

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'brand', 'category']
