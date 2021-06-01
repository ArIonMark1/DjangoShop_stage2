from django.shortcuts import render
import os
import json

# Create your views here.
views_dir = os.path.dirname(__file__)


def index(request):
    content = {'title': 'geekShop'}
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'geekshop products',
        'content': 'Hello User!!',
    }

    file_path = os.path.join(views_dir, 'fixtures/Product.json')
    content.update(json.load(open(file_path, encoding='utf-8')))
    # content['products'] = json.load(open(file_path, encoding='utf-8'))

    # print(content, '\n')
    return render(request, 'mainapp/products.html', content)
