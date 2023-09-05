from repositories.otpcodes_repository import GenerateOtp
from usecases.account.otpcodes_usecase import circuitbreaker, otp_failed
from rest_framework.response import Response
import random
import redis


def otp_sender(phone_number):
    code = GenerateOtp(phone_number=phone_number)

    def kavenegar():
        code.set_sender('kavenegar')
        print(f'kavenegar sent:{code.code}')
        success = random.choice([True, False])
        send_state_checker(code, success)

    def signal():
        code.set_sender('signal')
        print(f'signal sent:{code.code}')
        success = random.choice([True, False])
        send_state_checker(code, success)

    # todo: ENTEKHABE NAME KHOOB
    # todo: tamiz benevis
    stable_senders = circuitbreaker()
    sender = random.choice(stable_senders)

    match sender:
        case 'kavenegar':
            kavenegar()
        case 'signal':
            signal()


def send_state_checker(code, success):
    if success:
        code.success()
        return Response({'message': 'code sent'})
    else:
        otp_failed(code)
        otp_sender(code.phone_number)
