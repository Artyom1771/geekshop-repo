import os
import json
import datetime
from django.shortcuts import render

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
        'title': 'Geekshop - продукты'
    }
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context['products'] = json.load(open(file_path, encoding='utf-8'))
    return render(request, 'products/products.html', context)
