from django.forms import ModelForm
from products.models import Product


class ProductForm(ModelForm):
    model = Product