from repositories import otpcodes_repository
from django.utils import timezone


def CircuitBreaker(sender):
    '''returns False if sender was not stabel'''

    sender_state = otpcodes_repository.AllOtpCodes().filter(sender=sender, status='break',
                                          created__gte=timezone.now() - timezone.timedelta(hours=5))

    if sender_state.exists():
        return False
    return True


def OtpFailed(code):
    failed_count = otpcodes_repository.AllOtpCodes().filter(sender=code.sender, status='failed',
                                          created__gte=timezone.now() - timezone.timedelta(hours=5)).count()
    if failed_count >= 10:
        code.set_break()
    else:
        code.success(success=False)


def OtpValidator(phone_number, recived_code):
    '''returns True if the code is valid'''

    code = otpcodes_repository.Get_By_phone_number(phone_number)
    if code and code.code == recived_code and code.is_valid():
        code.success()
        return True
    return False
