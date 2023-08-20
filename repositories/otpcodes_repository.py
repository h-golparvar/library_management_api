from accounts.models import OtpCode
from django.utils import timezone


def CircuitBreaker(sender):
    '''returns False if sender was not stabel'''

    sender_state = OtpCode.objects.filter(sender=sender, status='break',
                                          created__gte=timezone.now() - timezone.timedelta(hours=5))

    if sender_state.exists():
        return False
    return True


def OtpFailed(code):
    failed_count = OtpCode.objects.filter(sender=code.sender, status='failed',
                                          created__gte=timezone.now() - timezone.timedelta(hours=5)).count()
    if failed_count >= 10:
        code.set_break()
    else:
        code.success(success=False)


def OtpValidator(phone_number, recived_code):
    '''returns True if the code is valid'''
    try:
        code = OtpCode.objects.filter(phone_number=phone_number).latest('id')
    except:
        return False
    if code and code.code == recived_code and code.created > timezone.now() - timezone.timedelta(minutes=5)\
            and code.status == 'pending':
        code.success()
        return True
    return False
