
from django.contrib import admin
from django.urls import path
from . import views
app_name="myapp"
urlpatterns = [
   
    

    path('',views.ProductList.as_view(), name='index'),
    path('<pk>/details', views.ProductDetail.as_view(), name='detail'),
    path('price/list', views.ProductPriceList.as_view(), name='price_list'),

]