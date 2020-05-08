from django.urls import path
from products.views import ProductList, ProductCreate


urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('product/create/', ProductCreate.as_view(), name='product-create')

]
