from django.db import models
from accounts.models import User
from django.utils import timezone


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


    @property
    def is_available(self):
        #latest_reservation = self.reservations.latest('start_date')
        try:
            if not self.reservations.latest('start_date').is_finished:
                return False
        except:
            return True


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.book} - {self.user}'


    @property
    def is_finished(self):
        if self.start_date.date() + timezone.timedelta(days=self.duration) < timezone.now().date():
            return True
        return False