from django.contrib import admin
from django.urls import include, path
from . import views
app_name = "base"
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginUser, name="login-user"),
    path('logout/', views.logoutUser, name="logout-user"),
    path('register/', views.registerUser, name="register-user"),
    path('main/', views.main, name="main"),
    path('add-book/', views.addBook, name="add-book"),
    path('show-book/<int:pk>/', views.showBook, name="show-book"),
    path('update-book/<int:pk>/', views.updateBook, name="update-book"),
]
