from accounts.models import OtpCode
from random import randint


def AllOtpCodes():
    return OtpCode.objects.all()

def OtpBySender(sender):
    return OtpCode.objects.filter(sender=sender)


def Get_By_phone_number(phone_number):
    return OtpCode.objects.filter(phone_number=phone_number).latest('id')


def GenerateOtp(phone_number, sender):
    code = randint(1000, 9999)
    code = OtpCode.objects.create(phone_number=phone_number, code=code, sender=sender)
    return code