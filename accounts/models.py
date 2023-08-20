from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from .managers import UserManager
import random
from django.utils import timezone


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    username = models.CharField(blank=True, null=True, max_length=1)
    membership_plan = models.ForeignKey('MemebershiPlan', blank=True, null=True, on_delete=models.CASCADE)
    membership_validity_date = models.DateTimeField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']


    def __str__(self):
        return self.get_full_name()


    @property
    def is_staff(self):
        return self.is_admin


    def ActiveNewMemebershiPlan(self, plan_id):
        try:
            plan = MemebershiPlan.objects.get(id=plan_id, is_active=True)
        except:
            return {'message': 'plan is not available'}

        if plan:
            self.membership_plan = plan
            self.membership_validity_date = timezone.now() + timezone.timedelta(days=plan.days)
            self.save()
            return {'message': 'plan successfuly activated'}


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.IntegerField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=10, default='pending')
    choices = (
        ('succeccful', 'succeccful'),
        ('failed', 'failed'),
        ('pending', 'pending'),
        ('break', 'break')
    )
    status = models.CharField(max_length=10, choices=choices, default='pending')


    def __str__(self):
        return f'{self.phone_number} - {self.code}'


    def generate(self, phone_number, sender):
        code = random.randint(1000,9999)
        code = self.objects.create(phone_number=phone_number, code=code, sender=sender)
        return code


    def success(self, success=True):
        if success:
            self.status = 'succeccful'
        else:
            self.status = 'failed'
        self.save()

    def set_break(self):
        self.status = 'break'
        self.save()


class MemebershiPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.PositiveIntegerField()
    days = models.PositiveIntegerField()
    is_active = models.BooleanField()


    def __str__(self):
        return f'{self.title} : {self.days} روزه'