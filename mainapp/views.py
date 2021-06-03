from django.shortcuts import render
import os
# import json

from mainapp.models import ProductCategory, Product


# Create your views here.
# views_dir = os.path.dirname(__file__)


def index(request):
    content = {'title': 'geekShop'}

    return render(request, 'mainapp/index.html', content)


def products(request, cat=None):
    content = {
        'title': 'geekshop products',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    if cat:

        content['products'] = Product.objects.filter(category_id=cat)
        return render(request, 'mainapp/products.html', content)
    else:
        return render(request, 'mainapp/products.html', content)

