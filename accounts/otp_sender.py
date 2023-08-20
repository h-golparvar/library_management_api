from .models import OtpCode
from django.utils import timezone
from repositories.otpcodes_repository import CircuitBreaker, OtpFailed


def OtpSender(phone_number):
    def kavenegar():
        code = OtpCode.generate(OtpCode, phone_number=phone_number, sender='kavenegar')
        print(f'kavenegar sent:{code.code}')
        success = True
        if success:
            return {'message': 'code sent'}
            code.success()
        else:
            OtpFailed(code)


    def signal():
        code = OtpCode.generate(OtpCode, phone_number=phone_number, sender='signal')
        print(f'signal sent:{code.code}')
        success = True
        if success:
            code.success()
        else:
            OtpFailed(code)

    if CircuitBreaker('kavenegar'):
        kavenegar()
    else:
        signal()



