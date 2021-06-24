from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # классы для работы с пагинацией страниц


from mainapp.models import ProductCategory, Product


# Create your views here.
# views_dir = os.path.dirname(__file__)


def index(request):
    content = {'title': 'geekShop'}

    return render(request, 'mainapp/index.html', content)


def products(request, value=None, page=1):
    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategory.objects.all()}

    site_products = Product.objects.filter(category_id=value) if value else Product.objects.all()

    paginator = Paginator(site_products, 3)
    # products_paginator = paginator.page(page)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    content['products'] = products_paginator

    return render(request, 'mainapp/products.html', content)
