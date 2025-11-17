from django.urls import path
from . import views 

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),  
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
]