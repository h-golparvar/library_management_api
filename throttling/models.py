from django.db import models
from django.utils import timezone


class ThrottlingLog(models.Model):
    ip = models.CharField(max_length=39)
    user_id = models.IntegerField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    caller = models.CharField(max_length=100)
    throttled = models.BooleanField(default=False)
    throttl_duration = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.ip} - {self.time}'


    def set_throttled(self, duration):
        self.throttled = True
        self.throttl_duration = int(duration)
        self.save()


    def is_throttled(self):
        if self.throttled and self.time + timezone.timedelta(seconds=self.throttl_duration) >= timezone.now():
            return True
        self.throttled = False
        self.save()
        return False