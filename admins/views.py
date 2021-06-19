from django.shortcuts import render

from users.models import User

# Create your views here.
# CRUD

# top page
def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin.html', context)


# READ
def admin_users(request):
    context = {'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


# CREATE
def admin_users_create(request):
    context = {}
    return render(request, 'admins/admin-users-create.html')


# UPDATE
def admin_users_update(request, id_user):
    return render(request, 'admins/admin-users-update-delete.html')


# DELETE
def admin_users_delete(request, id_user):
    pass
