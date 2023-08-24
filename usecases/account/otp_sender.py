from repositories.otpcodes_repository import GenerateOtp
from usecases.account.otpcodes_usecase import CircuitBreaker, OtpFailed
from rest_framework.response import Response


def OtpSender(phone_number):
    def kavenegar():
        code = GenerateOtp(phone_number=phone_number, sender='kavenegar')
        print(f'kavenegar sent:{code.code}')
        success = True
        if success:
            return Response({'message': 'code sent'})
            code.success()
        else:
            OtpFailed(code)


    def signal():
        code = GenerateOtp(phone_number=phone_number, sender='signal')
        print(f'signal sent:{code.code}')
        success = True
        if success:
            return Response({'message': 'code sent'})
            code.success()
        else:
            OtpFailed(code)

    if CircuitBreaker('kavenegar'):
        kavenegar()
    else:
        signal()



