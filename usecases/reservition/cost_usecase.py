from datetime import date
from django.utils import timezone


def CostCalculatorUsecase(user, duration):
    try:
        if user.membership_validity_date.date() >= date.today():
            return 0
    except:
        reservations = user.reservations
        reservations = reservations.filter(start_date__gt=timezone.now()-timezone.timedelta(days=60))
        total = sum(item.cost for item in reservations)
        if total > 300000:
            return 0
        else:
            cost = int(duration) * 1000
            reservations = reservations.filter(start_date__gt=timezone.now()-timezone.timedelta(days=30))
            if reservations.count() > 3:
                return int(cost * 70 /100)
            return cost
