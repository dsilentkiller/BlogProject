from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import SignUpForm
from blog.forms import *
from blog.models import *
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


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Your template name
    context_object_name = 'posts'
    ordering = ['-created_at']  # Optional: To order by created date

class PostCreateView(LoginRequiredMixin,CreateView):
    model =Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:list')

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:list')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    success_url = reverse_lazy('inventory:inventory_list')


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:list')

def base(request):
    return render(request, 'blog/base.html')