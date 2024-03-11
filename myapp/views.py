from msilib.schema import ListView
from typing import Any
from urllib import request
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Product 
from django.views.generic import ListView, DetailView,View

# Create your views here.

class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request,'product/base.html')

   

          
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

    
    
class ProductCategoryList(ListView):
    model=Product
    template_name="product/product_category.html"
    context_object_name = "list"
    def get_queryset(self):
        return Product.app_object.filter_by_category_name('device')
    
    
class SearchView(ListView):
    model = Product
    template_name = "product/product_search.html"
    def get_queryset(self):
        name = self.request.GET.get("name", "")
        return self.model.objects.filter(name__contains=name)

