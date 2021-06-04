from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm, UserCreationForm


# Create your views here.

def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            user = auth.authenticate(username=username, password=password)  # сверяем с базой, есть ли такой юзер
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {'title': 'GeekShop Авторизация', 'form': form}
    return render(request, 'login.html', context)


def register(request):
    context = {'title': 'GeekShop Регистрация'}
    return render(request, 'register.html', context)


def logout(request):
    auth.logout(request)
