from . import views
from django.urls import path

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_urls')
]