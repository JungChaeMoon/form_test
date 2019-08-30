from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .forms import PostCreateForm
from .models import Post


class PostListView(ListView):
    template_name = 'testapp/post_list.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'testapp/post_detail.html'
    model = Post


class PostCreateView(CreateView):
    template_name = 'testapp/post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('testapp:post_list')
