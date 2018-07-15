from django.forms import ModelForm
from app.models import Brand, Item, Category

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'brand', 'category']
