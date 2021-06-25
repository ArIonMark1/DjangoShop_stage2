from django.urls import path, re_path

from admins.views import *

app_name = 'admins'

urlpatterns = [
    path('', AdminIndexListView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='users_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='users_delete'),

    path('users/recovery/<int:id_user>/', admin_users_recovery, name='users_recovery'),

    path('categories/', CategoriesListView.as_view(), name='admin_categories'),
    path('categories/create/', CategoriesCreateListViews.as_view(), name='create_categories'),
    path('categories/update/<int:pk>/', CategoriesUpdateListViews.as_view(), name='categories_update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='categories_delete'),

    path('categories/recovery/<int:id_category>/', admin_categories_recovery, name='categories_recovery'),

    path('products/read/', ProductsListView.as_view(), name='admin_products'),
    path('products/create/', ProductsCreateListView.as_view(), name='create_products'),
    path('products/update/<int:pk>/', ProductsUpdateListView.as_view(), name='update_products'),
    path('products/delete/<int:pk>/', ProductsDeleteView.as_view(), name='delete_products'),

]
