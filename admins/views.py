from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from admins.forms import CategoryCreationForm, CategoriesAdminProfileForm, ProductAdminCreationForm
from django.contrib.auth.decorators import user_passes_test  # декоратор для обязательной авторизации
from users.models import User
from mainapp.models import ProductCategory, Product


# Create your views here.
# CRUD

# top page
@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin.html', context)


# READ
@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {'title': 'GeekShop - Admin | Пользователи', 'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


# CREATE
@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно!!')
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()

    context = {'title': 'GeekShop - Admin | Регистрация', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


# UPDATE
@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id_user=None):
    selected_user = User.objects.get(id=id_user)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Изменения данных пользователя "{selected_user}" успешно сохранены!!')
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)

    context = {'title': 'GeekShop - Admin | Пользователь',
               'form': form,
               'selected_user': selected_user,
               }
    return render(request, 'admins/admin-users-update-delete.html', context)


# DELETE
@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id_user):
    user = User.objects.get(id=id_user)
    user.is_active = False
    user.save()
    messages.success(request, f'Пользователь "{user}" успешно удален!!')
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_users_recovery(request, id_user):
    user = User.objects.get(id=id_user)
    user.is_active = True
    user.save()
    messages.success(request, f'Пользователь "{user}" успешно Востановлен!!')
    return HttpResponseRedirect(reverse('admins:admin_users'))


# =========================
# categories
# =========================

# READ = complete
@user_passes_test(lambda u: u.is_superuser)
def admin_categories_read(request):
    categories = ProductCategory.objects.all()
    context = {'title': 'GeekShop - Admin | Категории', 'categories': categories}
    return render(request, 'admins/admin-category-read.html', context)


# ====================================================================
# CREATE = complete
@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == 'POST':
        form = CategoryCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Категория успешно Создана!!')
            return HttpResponseRedirect(reverse('admins:admin_categories'))
        else:
            print(form.errors)
    else:
        form = CategoryCreationForm()
    context = {'title': 'GeekShop - Admin | Регистрация категории', 'form': form, }
    return render(request, 'admins/admin-categories-create.html', context)


# ====================================================================
@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request, id_category):
    category = ProductCategory.objects.get(id=id_category)

    if request.method == 'POST':

        form = CategoriesAdminProfileForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Изменения данных пользователя "{category}" успешно сохранены!!')
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = CategoriesAdminProfileForm(instance=category)

    context = {'title': 'GeekShop - Admin | Изменение категории',
               'form': form,
               'category': category}
    return render(request, 'admins/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_delete(request, id_category):
    category = ProductCategory.objects.get(id=id_category)
    category.is_active = False
    category.save()
    messages.success(request, f'Категория "{category}" Деактивированна!!')
    return HttpResponseRedirect(reverse('admins:admin_categories'))


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_recovery(request, id_category):
    category = ProductCategory.objects.get(id=id_category)
    category.is_active = True
    category.save()
    messages.success(request, f'Категория "{category}" успешно Востановленна!!')
    return HttpResponseRedirect(reverse('admins:admin_categories'))


# =========================
# products
# =========================
# READ
@user_passes_test(lambda u: u.is_superuser)
def admin_products_read(request):
    context = {'title': 'GeekShop - Admin | Товар',
               'admin_products': Product.objects.all(),
               'categories': ProductCategory.objects.all(),
               }
    return render(request, 'admins/admin-products-read.html', context)


# ============================================
# CREATE
@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            name = request.POST['name']
            messages.success(request, f'Товар "{name}" успешно Зарегистрирован!!')
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminCreationForm()
    context = {'title': 'GeekShop - Admin | Регистрация Товара',
               'form': form, }

    return render(request, 'admins/admin-products-create.html', context)


# UPDATE
@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, id_prod):
    selected_product = Product.objects.get(id=id_prod)

    if request.method == 'POST':

        form = ProductAdminCreationForm(data=request.POST, instance=selected_product, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Изменения данных пользователя "{selected_product}" успешно сохранены!!')
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminCreationForm(instance=selected_product)

    context = {'title': 'GeekShop - Admin | Изменение категории',
               'form': form,
               'product': selected_product}

    return render(request, 'admins/admin-products-update-delete.html', context)


# DELETE
@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, id_prod):
    selected_product = Product.objects.get(id=id_prod)
    selected_product.delete()
    messages.success(request, f'Товар "{selected_product}" Удален!!')
    return HttpResponseRedirect(reverse('admins:admin_products'))

# RECOVERY
