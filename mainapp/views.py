from django.shortcuts import render

from mainapp.models import ProductCategory, Product


# Create your views here.
# views_dir = os.path.dirname(__file__)


def index(request):
    content = {'title': 'geekShop'}

    return render(request, 'mainapp/index.html', content)


def products(request, value=None):
    content = {
        'title': 'geekshop products',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }

    if value:
        for product in content['products']:
            id_categories = product.category_id
            if id_categories == value:
                content['products'] = Product.objects.filter(category_id=value)
                return render(request, 'mainapp/products.html', content)

    return render(request, 'mainapp/products.html', content)
