from users.forms import UserRegistrationForm, UserProfileForm

from mainapp.models import ProductCategory, Product
from django import forms

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
        'class': 'form-control py-4', 'placeholder': 'Enter the name of the category',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Product description'
    }))
    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-control py-4'}), required=False)

    class Meta:
        model = ProductCategory
        fields = '__all__'


class CategoriesAdminProfileForm(CategoryCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter the name of the category',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Product description'
    }))

    model = ProductCategory
    fields = '__all__'


# --------------------------------------------------------------------
# ============================ products ============================
# --------------------------------------------------------------------

class ProductAdminCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter product name'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter product description'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter product price'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter quantity'}))

    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'form-control'}))

    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-control py-4'}), required=False)

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category', 'is_active')


class ProductAdminUpdateForm(ProductAdminCreationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'}), required=False)

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category', 'is_active')
