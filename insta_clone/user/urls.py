from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.UserProfileView.as_view(),
         name="user-profile"),
    path('signup/', views.RegisterUser.as_view(), name="user-reg"),
    path('login/', views.UserLoginView.as_view(), name="user-login"),
    path('logout/', views.UserLogout.as_view(), name="user-logout"),

    path('update-user/<int:pk>/', views.UserUpdate.as_view(), name="user-up"),
]
