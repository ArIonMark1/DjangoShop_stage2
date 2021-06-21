from django.urls import path

from admins.views import *

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users/create/', admin_users_create, name='users_create'),
    path('users/update/<int:id_user>/', admin_users_update, name='users_update'),
    path('users/delete/<int:id_user>/', admin_users_delete, name='users_delete'),
    path('users/recovery/<int:id_user>/', admin_users_recovery, name='users_recovery'),

    path('categories/', admin_categories_read, name='admin_categories'),
    path('categories/create/', admin_categories_create, name='create_categories'),
    path('categories/update/<int:id_category>/', admin_categories_update, name='categories_update'),
    path('categories/delete/<int:id_category>/', admin_categories_delete, name='categories_delete'),
    path('categories/recovery/<int:id_category>/', admin_categories_recovery, name='categories_recovery'),

]
