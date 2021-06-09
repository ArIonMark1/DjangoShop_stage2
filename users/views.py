from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)  # сверяем с базой, есть ли такой юзер

            if user and user.is_active:
                auth.login(request, user)

                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {'title': 'GeekShop Авторизация', 'form': form}
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)  # если заполненая
        if form.is_valid():
            form.save()  # должно сохранять в базу
            messages.success(request, 'Регистрация прошла успешно!!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()  # если пустая

    context = {'title': 'GeekShop Регистрация', 'form': form}
    return render(request, 'register.html', context)


def profile(request):

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные изменены!!')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    content = {'title': 'GeekShop - Профиль', 'form': form}
    return render(request, 'profile.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
