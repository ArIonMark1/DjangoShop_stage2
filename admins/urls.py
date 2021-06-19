from django.urls import path

from admins.views import *

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users/create/', admin_users_create, name='users_create'),
    path('users/update/<int:id_user>/', admin_users_update, name='users_update'),
    path('users/delete/<int:id_user>/', admin_users_delete, name='users_delete'),

]
