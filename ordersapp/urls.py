from django.urls import path
from ordersapp.views import OrderList, OrderItemsCreate, OrderUpdate, OrderDelete, OrderRead

app_name = 'ordersapp'

urlpatterns = [
    path('', OrderList.as_view(), name='orders_list'),
    path('create/', OrderItemsCreate.as_view(), name='order_create'),
    path('read/<int:pk>/', OrderRead.as_view(), name='order_read'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='order_delete'),
    #
    # path('forming/complete/<int:pk>/', OrderItemsCreate.as_view(), name='order_forming_complete'),

]
