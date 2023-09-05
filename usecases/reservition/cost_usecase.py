from datetime import date
from django.utils import timezone


def cost_calculator_usecase(user, duration):
    if user.membership_validity_date is not None and user.membership_validity_date.date() >= date.today():
        return 0
    else:
        reservations = user.reservations
        reservations = reservations.filter(start_date__gt=timezone.now()-timezone.timedelta(days=60))
        total_recent_reservations_cost = sum(item.cost for item in reservations)
        if total_recent_reservations_cost > 300000:
            return 0
        else:
            cost = int(duration) * 1000
            reservations = reservations.filter(start_date__gt=timezone.now()-timezone.timedelta(days=30))
            if reservations.count() > 3:
                return int(cost * 70 / 100)
            return cost
