from usecases.account.otpcodes_usecase import OtpValidator
from rest_framework_simplejwt.tokens import RefreshToken
from usecases.account.otp_sender import OtpSender
from django.shortcuts import get_object_or_404
from accounts.models import User


def identify(data):
        if data.get('code'):
            otp_state = OtpValidator(phone_number=data['phone_number'], recived_code=data['code'])
            if otp_state :
                user = get_object_or_404(User, phone_number=data['phone_number'])
                refresh = RefreshToken.for_user(user)
                return {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            else:
                return {'message': 'code is not valid'}
        else:

            return OtpSender(data['phone_number'])


def TokenRevoker(refresh_token):
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
        return {'message': 'token revoked'}
    except Exception as e:
        return {'message': 'error'}