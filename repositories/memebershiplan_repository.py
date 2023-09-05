from accounts.models import MemebershiPlan


def all_memebershi_plans():
    return MemebershiPlan.objects.all()
