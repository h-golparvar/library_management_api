from repositories import otpcodes_repository
from django.utils import timezone
from library import settings
import redis


r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def circuitbreaker():
    """returns all stable senders list"""
    senders = settings.senders
    stables = []
    for sender in senders:
        if is_sender_stable(sender):
            stables.append(sender)
    return stables


def is_sender_stable(sender):
    faileds_number = r.get(sender+'_error_count')
    if r.exists(sender+'_validity'):
        return False

    if faileds_number and int(faileds_number) >= 3:
        r.set(sender+'_error_count', 0)
        r.set(sender+'_validity', 'False')
        r.expire(sender+'_validity', 1800)
    return True


def otp_failed(code):
    sender_error_count = r.get(code.sender+'_error_count')
    if sender_error_count:
        r.set(code.sender+'_error_count', int(sender_error_count) + 1)
    else:
        r.set(code.sender+'_error_count', 1)
    r.expire(code.sender+'_error_count', 300)


def otp_code_validator(phone_number, recived_code):
    """returns True if the code is valid"""

    code = otpcodes_repository.Get_By_phone_number(phone_number)
    if code and code.code == recived_code and code.is_valid():
        code.success()
        return True
    return False
