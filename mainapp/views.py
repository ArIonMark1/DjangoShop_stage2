from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # classes for working with page pagination

from mainapp.models import ProductCategory, Product


# Create your views here.


def index(request):
    content = {'title': 'geekShop'}

    return render(request, 'mainapp/index.html', content)


def products(request, value=None, page=1):
    content = {
        'title': 'Geekshop - Catalog',
        'categories': ProductCategory.objects.filter(is_active=True)}  # better method check if category is_valid

    site_products = Product.objects.filter(category_id=value, is_active=True, category__is_active=True) if value else \
        Product.objects.filter(is_active=True, category__is_active=True)

    paginator = Paginator(site_products, 3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    content['products'] = products_paginator

    return render(request, 'mainapp/products.html', content)
