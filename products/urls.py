from . import views
from django.urls import path

urlpatterns = [
    path('shop/', views.ProductList.as_view(), name='shop')
]