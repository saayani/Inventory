from django.forms import ModelForm
from app.models import Brand

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
