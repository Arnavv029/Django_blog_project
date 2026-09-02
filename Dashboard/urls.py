from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # categories endpoints
    path('categories/', views.categories, name='categories'),
    path('add_categories/', views.add_categories, name='add_categories'),
    path('edit_categories/<int:pk>/', views.edit_categories, name='edit_categories'),
    path('delete_categories/<int:pk>/', views.delete_categories, name='delete_categories'),
    # posts endpoints
    path('posts/', views.posts, name='posts'),
    path('add_posts/', views.add_posts, name='add_posts'),
    path('edit_posts/<int:pk>/', views.edit_posts, name='edit_posts'),
    path('delete_posts/<int:pk>/', views.delete_posts, name='delete_posts')
]
