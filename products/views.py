import os
import datetime
from django.shortcuts import render
from products.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
mydate = datetime.datetime.now()


def index(request):
    context = {
        'mydate': mydate,
        'title': 'Geekshop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'mydate': mydate,
        'title': 'Geekshop - продукты',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
