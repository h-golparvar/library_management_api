from django.contrib import admin
from .models import Book, City, Author, Genre, Reservation


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(City)
admin.site.register(Reservation)

