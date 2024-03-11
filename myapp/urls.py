
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name="myapp"
urlpatterns = [
   
    
    path('',views.Base.as_view(),name='base'),
    path('list/',views.ProductList.as_view(), name='index'),
    path('<pk>/details', views.ProductDetail.as_view(), name='detail'),
    path('price/list', views.ProductPriceList.as_view(), name='price_list'),
    path('category/list/', views.ProductCategoryList.as_view(), name='category_list'),
    path('search/', views.SearchView.as_view(), name='search'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)