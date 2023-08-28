from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = [
    path('books/', views.BooksListView.as_view()),
    path('book/', views.BookReservationView.as_view()),
    path('book/<int:id>/', views.BookEditDeleteView.as_view()),
    path('book/add/', views.BookAddView.as_view()),
]