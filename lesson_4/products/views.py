from django.views.generic import ListView, CreateView
from products.models import Product
from products.forms import ProductForm


class BaseProduct:
    model = Product
    fields = ['title', 'price', 'unit', 'receipt_date', 'provider_name']

    class Meta:
        abstract = True


class ProductList(BaseProduct, ListView):

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title_page': 'Список продуктов'
        })
        return context


class ProductCreate(BaseProduct, CreateView):
    success_url = '/'
    fields = ['title', 'price']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title_page': 'Регистрация продукта'
        })
        return context
