from django.urls import path
from ordersapp.views import IndexView

app_name = 'ordersapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
