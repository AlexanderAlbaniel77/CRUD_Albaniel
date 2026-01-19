from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomePageView,
    AboutPageView,
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    RegisterView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

    # Recipe URLs
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
]