# from django.shortcuts import render
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # classes for working with page pagination
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from mainapp.models import ProductCategory, Product


# Create your views here.

class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop'
        return context


class ProductsView(ListView):
    template_name = 'mainapp/products.html'
    model = Product
    paginate_by = 6

    def get_queryset(self):
        queryset = super(ProductsView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(is_active=True)
        return context

# =============== function products ===============
# =================================================

# def products(request, value=None, page=1):
#     content = {
#         'title': 'Geekshop - Catalog',
#         'categories': ProductCategory.objects.filter(is_active=True)}  # better method check if category is_valid
#
#     site_products = Product.objects.filter(category_id=value, is_active=True,
#     category__is_active=True) if value else \
#         Product.objects.filter(is_active=True, category__is_active=True)
#
#     paginator = Paginator(site_products, 6)
#
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#
#     content['products'] = products_paginator
#
#     return render(request, 'mainapp/products.html', content)
