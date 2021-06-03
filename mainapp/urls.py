from django.urls import path

from mainapp.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index')
]




