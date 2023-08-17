from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = [
    path('books/', views.BooksListView.as_view()),
    path('book/<int:pk>/', views.BookEditView.as_view()),
    path('book/add/', views.BookAddView.as_view()),
]