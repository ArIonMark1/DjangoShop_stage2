from django.urls import path

from mainapp.views import ProductsView

app_name = 'mainapp'

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('<int:category_id>/', ProductsView.as_view(), name='category'),
    path('page/<int:page>/', ProductsView.as_view(), name='page'),
]
