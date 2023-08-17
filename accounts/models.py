from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from .managers import UserManager
import random

class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    username = models.CharField(max_length=15, unique=False)
    choices = (
        ('Special', 'Special '),
        ('Normal', 'Normal')
    )
    membership = models.CharField(choices=choices, max_length=7, default='Normal')
    membership_validity_date = models.DateTimeField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']


    def __str__(self):
        return self.full_name


    @property
    def is_staff(self):
        return self.is_admin


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.IntegerField(blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.phone_number} - {self.code}'


    def generate(self, phone_number):
        code = random.randint(1000,9999)
        self.objects.create(phone_number=phone_number, code=code)
        return code
