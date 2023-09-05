from datetime import date
from datetime import datetime
from django.utils.dateparse import parse_date


def duration_validiator_usecase(user, duration):
    if user.membership_validity_date:
        membership_validity = user.membership_validity_date.date() - date.today()
        if duration < membership_validity.days and duration <= 14:
            return 'valid'
        elif duration < membership_validity.days:
            return {'message':'the duration cant exceed your membership validity time'}
        elif duration < membership_validity.days and duration > 14:
            return {'message':'maximum valid duration is 14 in your membership'}
    if duration <= 7:
        return 'valid'
    else:
        return {'message': 'maximum valid duration is 7 in your membership'}

