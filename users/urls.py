from django.urls import path

import users.views as auth

app_name = 'users'

urlpatterns = [
    path('login/', auth.login, name='login'),
    path('register/', auth.register, name='register'),
    path('logout/', auth.logout, name='logout'),
]
