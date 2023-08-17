from django.db import models
from accounts.models import User


class City(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=300)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='authors')

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Book (models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    author = models.ManyToManyField(Author,related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    publication = models.DateTimeField()
    shabak = models.IntegerField()
    price = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.title} از {self.author.name}'

