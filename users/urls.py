from django.urls import path

import users.views as auth
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [

    path('register/', auth.UserCreateView.as_view(), name='register'),
    path('login/', auth.LoginUsersView.as_view(), name='login'),
    path('profile/', auth.profile, name='profile'),
    path('logout/', auth.LogoutUserView.as_view(), name='logout'),
    path('verify/<email>/<activation_key>/', auth.verify, name='verify'),
]
