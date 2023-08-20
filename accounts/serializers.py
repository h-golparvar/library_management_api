from rest_framework import serializers
from .models import OtpCode, MemebershiPlan


class OtpCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpCode
        fields = '__all__'


class MemebershiPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemebershiPlan
        fields = '__all__'
