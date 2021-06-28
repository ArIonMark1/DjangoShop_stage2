from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from admins.forms import CategoryCreationForm, CategoriesAdminProfileForm, ProductAdminCreationForm, \
    ProductAdminUpdateForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test  # decorator for mandatory authorisation

from django.views.generic import TemplateView
from django.views.generic.list import ListView  # for using Class Based Views
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # for create objects and Update

from users.models import User
from mainapp.models import ProductCategory, Product


# Create your views here.
# CRUD

class AdminIndexListView(TemplateView):  # here better than ListView ???
    template_name = 'admins/admin.html'

    # queryset = False  # necessary for ListView !!!

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AdminIndexListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))  # admin validation decorator
    def dispatch(self, request, *args, **kwargs):
        return super(AdminIndexListView, self).dispatch(request, *args, **kwargs)


# ===========================================================

# ===========================================================
# ==================== CLASS READ ===========================

class UserListView(ListView):  # inheriting from the built-in class ListView
    model = User  # model of our class User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin | Users'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))  # admin validation decorator
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# ===========================================================

# ===========================================================
# ==================== CLASS CREATE =========================

class UserCreateView(CreateView, SuccessMessageMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_message = f'User has been Created!!!'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin | Registration'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


# ===========================================================

# ===========================================================
# ==================== CLASS UPDATE =========================

class UserUpdateView(UpdateView, SuccessMessageMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_message = 'User profile has been Changed '
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin | User'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


# ===========================================================

# ===========================================================
# ==================== CLASS DELETE =========================

class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args,
               **kwargs):  # overrides the delete method from complete deletion to user inactivity
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# ===========================================================


@user_passes_test(lambda u: u.is_superuser)
def admin_users_recovery(request, id_user):
    user = User.objects.get(id=id_user)
    user.is_active = True
    user.save()
    messages.success(request, f'User "{user}" successfully restored !!!')
    return HttpResponseRedirect(reverse('admins:admin_users'))


# ==================== CLASS RECOVERY =========================

# =============================================================


# =========================
# categories
# =========================

# ====================================================================
# ==================== CLASS READ CATEGORIES =========================

class CategoriesListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoriesListView, self).get_context_data(**kwargs)
        context['title'] = ' GeekShop - Admin | Categories '
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoriesListView, self).dispatch(request, *args, **kwargs)


# ====================================================================

# ====================================================================
# =================== CLASS CREATE CATEGORIES ========================

class CategoriesCreateListViews(CreateView, SuccessMessageMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = CategoryCreationForm
    success_url = reverse_lazy('admins:admin_categories')
    success_message = 'Category has been created !!!'

    def get_context_data(self, **kwargs):
        context = super(CategoriesCreateListViews, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin | Category registration'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoriesCreateListViews, self).dispatch(request, *args, **kwargs)


# ====================================================================

# ====================================================================
# =================== CLASS UPDATE CATEGORIES ========================

class CategoriesUpdateListViews(UpdateView, SuccessMessageMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoriesAdminProfileForm
    success_url = reverse_lazy('admins:admin_categories')
    success_message = 'Category has been Changed !!!'

    def get_context_data(self, **kwargs):
        context = super(CategoriesUpdateListViews, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin | Change category'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoriesUpdateListViews, self).dispatch(request, *args, **kwargs)


# ====================================================================

# ====================================================================
# =================== CLASS DELETE CATEGORIES ========================

class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# ====================================================================

# RECOVERY
@user_passes_test(lambda u: u.is_superuser)
def admin_categories_recovery(request, id_category):
    category = ProductCategory.objects.get(id=id_category)
    category.is_active = True
    category.save()
    messages.success(request, f'Category "{category}" successfully restored!!')
    return HttpResponseRedirect(reverse('admins:admin_categories'))


# ====================================================================
# ==================== CLASS READ PRODUCTS ===========================

class ProductsListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin | Product'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsListView, self).dispatch(request, *args, **kwargs)


# ====================================================================

# ====================================================================
# ==================== CLASS CREATE PRODUCTS =========================

class ProductsCreateListView(CreateView):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductAdminCreationForm
    success_url = reverse_lazy('admins:admin_products')

    def get_context_data(self, **kwargs):
        context = super(ProductsCreateListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin | Product registration'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsCreateListView, self).dispatch(request, *args, **kwargs)


# ====================================================================

# ====================================================================
# ==================== CLASS UPDATE PRODUCTS =========================

class ProductsUpdateListView(UpdateView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductAdminUpdateForm
    success_url = reverse_lazy('admins:admin_products')

    def get_context_data(self, **kwargs):
        context = super(ProductsUpdateListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin | Change category'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsUpdateListView, self).dispatch(request, *args, **kwargs)


# ====================================================================

# ====================================================================
# ==================== CLASS DELETE PRODUCTS =========================

class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')

# ====================================================================
