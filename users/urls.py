from django.urls import path

import users.views as auth

app_name = 'users'

urlpatterns = [

    path('register/', auth.register, name='register'),
    path('login/', auth.login, name='login'),
    path('profile/', auth.profile, name='profile'),
    path('logout/', auth.logout, name='logout'),
]
