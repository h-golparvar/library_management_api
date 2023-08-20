from django.shortcuts import render
from rest_framework.views import APIView
from .models import MemebershiPlan
from .serializers import OtpCodeSerializer, MemebershiPlanSerializer
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from usecases.account.identify_usecase import identify, TokenRevoker
from accounts.serializers import OtpCodeSerializer


class IdentifyView(APIView):
    throttle_scope = 'otp_hour_throttle'

    def post(self,request):
        srz_data = OtpCodeSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data = srz_data.data
            return Response(identify(srz_data))
        return srz_data.errors


class TokenRevoke(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        return Response(TokenRevoker(refresh_token))


class MemebershiPlansListView(ListAPIView):
    serializer_class = MemebershiPlanSerializer
    queryset = MemebershiPlan.objects.all()


class ActiveMemebershiPlansView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        success = True

        if success:
            return Response(request.user.ActiveNewMemebershiPlan(plan_id=request.POST['membership_plan_id']))
        else:
            return Response({'message': 'payment failed'})

