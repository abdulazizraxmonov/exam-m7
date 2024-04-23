from rest_framework import serializers
from .models import NATO_Member


class NATO_MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NATO_Member
        fields = '__all__'
