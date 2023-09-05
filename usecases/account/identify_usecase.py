from usecases.account.otpcodes_usecase import otp_code_validator
from rest_framework_simplejwt.tokens import RefreshToken
from usecases.account.otp_sender import otp_sender
from django.shortcuts import get_object_or_404
from accounts.models import User


def identify(data):
        if data.get('code'):
            otp_state = otp_code_validator(phone_number=data['phone_number'], recived_code=data['code'])
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

            return otp_sender(data['phone_number'])


def token_revoker(refresh_token):
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
        return {'message': 'token revoked'}
    except Exception as e:
        return {'message': 'error'}