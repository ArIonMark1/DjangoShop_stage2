from django.urls import path

from mainapp.views import products

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('<int:value>/', products, name='category'),
    path('page/<int:page>/', products, name='page'),
]




