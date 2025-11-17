from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

class HomePageView(TemplateView):
    template_name = "app/home.html"

class AboutPageView(TemplateView):
    template_name = "app/About.html"

class BlogListView(ListView):
    model = Post
    template_name = "app/blog_list.html"
    context_object_name = "posts"

class BlogDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "app/blog_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "app/blog_create.html"
    fields = ['title', 'body', 'author']
    success_url = '/blog/'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "app/blog_update.html"
    fields = ['title', 'body']
    success_url = '/blog/'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "app/blog_delete.html"
    success_url = '/blog/'