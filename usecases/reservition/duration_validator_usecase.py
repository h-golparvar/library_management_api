from datetime import date
from datetime import datetime
from django.utils.dateparse import parse_date


def DurationValidiatorUsecase(user, duration):
    if user.membership_validity_date:
        membership_validity = user.membership_validity_date.date() - date.today()
        if duration < membership_validity.days and duration <= 14:
            return 'vlaid'
        elif duration < membership_validity.days:
            return {'message':'the duration cant exceed your membership validity time'}
        elif duration < membership_validityand.days and duration > 14:
            return {'message':'maximum valid duration is 14 in your memebership'}
    if duration <=7:
        return 'vlaid'
    else:
        return {'message':'maximum valid duration is 7 in your memebership'}

