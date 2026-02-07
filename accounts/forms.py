from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    """
    User registration form with email, username, and password.
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-custom',
            'placeholder': 'Enter your email'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-custom',
            'placeholder': 'Choose a username'
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-custom',
            'placeholder': 'Create a password'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-custom',
            'placeholder': 'Confirm your password'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    """
    User login form with styled fields.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-custom',
            'placeholder': 'Username or Email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-custom',
            'placeholder': 'Enter your password'
        })
    )


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user profile information.
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'company']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-custom'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'company': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
        }
