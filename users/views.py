from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
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
        return super(UserProfileView, self).dispatch(**kwargs)


# ===============================================================
# ====================== CLASS LOGOUT ===========================
# ------- second variant logout -------

class LogoutUserView(LogoutView):
    pass

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
