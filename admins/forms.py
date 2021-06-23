from django.forms import ModelChoiceField

from users.forms import UserRegistrationForm, UserProfileForm
# ProductAdminCreationForm
from mainapp.models import ProductCategory, Product
from django import forms
# from django.forms.models import ModelForm
from users.models import User


# --------------------------------------------------------------------
# ============================ users ===============================
# --------------------------------------------------------------------
class UserAdminRegisterForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'image', 'email', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': False}))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'readonly': False}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')


# --------------------------------------------------------------------
# ============================ categories ==========================
# --------------------------------------------------------------------
class CategoryCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя категории',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Описание товара'
    }))
    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-control py-4'}), required=False)

    class Meta:
        model = ProductCategory
        fields = '__all__'


class CategoriesAdminProfileForm(CategoryCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя категории',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Описание товара'
    }))

    model = ProductCategory
    fields = '__all__'


# --------------------------------------------------------------------
# ============================ products ============================
# --------------------------------------------------------------------

class ProductAdminCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4'}))

    # category = forms.ChoiceField(widget=forms.Input(attrs={
    #     'class': 'form-control py-4'}))

    category = ModelChoiceField(queryset=ProductCategory.objects.all())

    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-control py-4'}), required=False)

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category', 'is_active')
