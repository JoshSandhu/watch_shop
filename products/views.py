from django.shortcuts import render
from django.views import generic
from .models import Product

# Create your views here.

class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.filter(satus=1.order_by('-created_on'))
    template_name = 'index.html'
    paginate_by = 6
    
