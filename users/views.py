from django.conf import settings
from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

from baskets.models import Basket
from users.models import User


# Create your views here.

# ====================== CLASS LOGIN ============================
class LoginUsersView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super(LoginUsersView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop Authorization'
        return context


# ===============================================================
# ==================== CLASS REGISTER ===========================

class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Registration Completed Successfully!!!'

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()

            if send_verify_mail(user):
                print('сообщение подтверждения отправленно')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                print('ошибка отправки!!')
                return HttpResponseRedirect(reverse('users:login'))
        else:
            form = UserCreateView.form_class()

        return super(UserCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)

        context['title'] = 'GeekShop Registration'
        return context


# ===============================================================
# ===================== CLASS PROFILE ===========================

class UserProfileView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'profile.html'
    success_message = 'Your profile has been changed'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserProfileView, self).dispatch(request, *args, **kwargs)


# ===============================================================
# ====================== CLASS LOGOUT ===========================
# ------- second variant logout -------

class LogoutUserView(LogoutView):
    pass


# ===============================================================
# ============= verify email ====================================

def verify(request, email, activation_key):
    user = User.objects.filter(email=email).first()
    if user:
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')

    return render(request, 'verify.html')


def send_verify_mail(user):
    # тема сообщения, само сообщение, почта на которую отправлять
    subject = 'Verify your account'
    link = reverse('users:verify', args=[user.email, user.activation_key])
    message = f'{settings.DOMAIN}{link}'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

# ===============================================================
# ------- login function -------
# ------------------------------
# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)  # сверяем с базой, есть ли такой юзер
#
#             if user and user.is_active:
#                 auth.login(request, user)
#
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#
#     context = {'title': 'GeekShop Авторизация', 'form': form}
#     return render(request, 'login.html', context)

# ===============================================================
# ------- profile function -------
# --------------------------------

# @login_required
# def profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, instance=user, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Данные изменены!!')
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=user)
#
#     context = {'title': 'GeekShop - Профиль',
#                'form': form,
#                'baskets': Basket.objects.filter(user=user),
#                }
#     return render(request, 'profile.html', context)

# ====================================
# ------- first variant logout -------

# class LogoutUserView(View):
#     def get(self, request):
#         auth.logout(request)
#         return HttpResponseRedirect(reverse('index'))

# ------- functional variant logout -------
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))
