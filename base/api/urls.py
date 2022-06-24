from django.contrib import admin
from django.urls import include, path
from . import views
app_name = "base"
urlpatterns = [
    path('books/', views.book_list, name="book-list"),
    path('book/<str:pk>/', views.books_details, name="books_details"),
]
