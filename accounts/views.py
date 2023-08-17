from django.shortcuts import render
from rest_framework.views import APIView
from .models import OtpCode
from .serializers import OtpCodeSerializer
from rest_framework.response import Response
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .otp_sender import OtpSender
from rest_framework import status


class IdentifyView(APIView):
    throttle_scope = 'otp_hour_throttle'

    def post(self,request):
        srz_data = OtpCodeSerializer(data = request.POST)
        if srz_data.is_valid():
            srz_data = srz_data.data
            if 'code' in srz_data:
                code = OtpCode.objects.filter(phone_number=srz_data['phone_number']).latest('id')
                if code and code.code == srz_data['code'] and code.created > timezone.now()-timezone.timedelta(minutes=5):
                    user = User.objects.get(phone_number=srz_data['phone_number'])
                    refresh = RefreshToken.for_user(user)
                    return Response ({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    })
                else:
                    return Response({'message':'code in not valid'})
            else:
                code = OtpCode.generate(OtpCode, phone_number=srz_data['phone_number'])
                OtpSender(code)
                return Response({'message': 'code sent'}, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenRevoke(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message':'token revoked'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)