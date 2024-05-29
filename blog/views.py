from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.views import LoginView,LogoutView


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
      
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    


class LoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class LogoutView(LogoutView):
    next_page = '/'  # Redirect to home after logout