from django.contrib import admin
from django.urls import include, path

from user import views



urlpatterns = [
    path('register/', views.register,name="register"),
    path('login/', views.loginUser,name="login"),
    path('logout/', views.logoutUser,name="logout"),
]
