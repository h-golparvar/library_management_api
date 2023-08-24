from accounts.models import MemebershiPlan


def AllMemebershiPlans():
    return MemebershiPlan.objects.all()
