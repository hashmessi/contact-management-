from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import UserRegisterForm, UserLoginForm


class UserRegisterView(CreateView):
    """
    User registration view.
    Creates a new user and logs them in automatically.
    """
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('contacts:contact_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Auto-login after registration
        login(self.request, self.object)
        messages.success(self.request, f'Welcome to ZENVIO, {self.object.username}!')
        return response
    
    def dispatch(self, request, *args, **kwargs):
        # Redirect logged-in users to contacts
        if request.user.is_authenticated:
            return redirect('contacts:contact_list')
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(LoginView):
    """
    User login view with custom template and form.
    """
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    """
    User logout view.
    """
    next_page = 'home'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You have been logged out.')
        return super().dispatch(request, *args, **kwargs)
