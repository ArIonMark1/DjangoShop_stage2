import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User, ProfileUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control  py-4', 'placeholder': 'Enter your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control  py-4', 'placeholder': 'Enter password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control  py-4', 'placeholder': 'Enter first_name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter last_name'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter username'
    }))
    # email = forms.EmailField(widget=forms.TextInput(attrs={
    #     'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Repeat password'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save()
        user.is_active = False

        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()

        user.save()
        return user


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'readonly': True}))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'readonly': True}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')


class AdditionUserProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ('gender', 'tagline', 'description',)

        widgets = {
            'gender': forms.Select(attrs={
                'class': 'form-control'}),
            'tagline': forms.TextInput(attrs={
                'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control'}),

        }
