from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_routes),
    path('get-posts/', views.get_posts),
    path('get-posts/<int:pk>/', views.get_post),
]
