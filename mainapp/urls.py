from django.urls import path

from mainapp.views import products

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('<int:cat>/', products, name='category'),
]




