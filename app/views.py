from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Recipe


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')


class HomePageView(TemplateView):
    template_name = "app/home.html"

class AboutPageView(TemplateView):
    template_name = "app/about.html"


class RecipeListView(ListView):
    model = Recipe
    template_name = "app/recipe_list.html"
    context_object_name = "recipes"

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = "recipe"
    template_name = "app/recipe_detail.html"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "app/recipe_create.html"
    fields = ['title', 'description', 'instructions', 'category']
    success_url = reverse_lazy('recipe_list')
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "app/recipe_update.html"
    fields = ['title', 'description', 'instructions', 'category']
    success_url = reverse_lazy('recipe_list')
    

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "app/recipe_delete.html"
    success_url = reverse_lazy('recipe_list')
    