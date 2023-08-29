from throttling.models import ThrottlingLog
from django.utils import timezone


def GetLogs(ip, user_id, period):
    if period == 'hour':
        timedelta = timezone.timedelta(hours=1)
    elif period == 'min':
        timedelta = timezone.timedelta(minutes=2)

    if user_id:
        return ThrottlingLog.objects.filter(user_id=user_id, time__gt=timezone.now()-timedelta)
    if ip:
        return ThrottlingLog.objects.filter(ip=ip, time__gt=timezone.now()-timedelta)


def GetLastLog(ip, user_id):
    try:
        if user_id:
            return ThrottlingLog.objects.filter(user_id=user_id).latest('id')
        if ip:
            return ThrottlingLog.objects.filter(ip=ip).latest('id')
    except:
        return None


def AddLog(ip, user_id, caller):
    ThrottlingLog.objects.create(
        ip=ip,
        user_id = user_id,
        caller = caller,
        )