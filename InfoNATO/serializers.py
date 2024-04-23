from rest_framework import serializers
from .models import InfoNATO

class InfoNATOSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoNATO
        fields = '__all__'