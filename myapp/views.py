from msilib.schema import ListView
from django.shortcuts import render
from .models import Product 
from django.views.generic import ListView, DetailView

# Create your views here.



          
class ProductList(ListView):
    model=Product
    context_object_name="productsss"
    template_name="product/product_list.html"
    
    
    
class ProductDetail(DetailView):
    model=Product
    
    template_name="product/product_detail.html"

class ProductPriceList(ListView):
    model=Product
    context_object_name="product"
    template_name="product/product_price.html"
    def get_queryset(self):
        return Product.app_object.all()

    
# class ProductCategoryList(ListView):
#     model=Product
#     template_name="product/product_category.html"
#     def get_queryset(self):
#         return Product.app_object.all()
    

    