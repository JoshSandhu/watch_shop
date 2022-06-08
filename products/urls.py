from . import views
from django.urls import path

urlpatterns = [
    path('shop/', views.ProductList.as_view(), name='shop'),
    path('<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('like/<slug:slug>', views.ProductLike.as_view(), name='product_like'),
]