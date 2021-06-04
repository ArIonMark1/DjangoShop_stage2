from django.shortcuts import render

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
        for product in content['products']:
            id_categories = product.category_id
            if id_categories == cat:
                content['products'] = Product.objects.filter(category_id=id_categories)
                return render(request, 'mainapp/products.html', content)
    else:
        return render(request, 'mainapp/products.html', content)
