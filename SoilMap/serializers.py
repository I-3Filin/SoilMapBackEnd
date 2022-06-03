from rest_framework import serializers
from SoilMap.Models import CesiumActivity

class CesiumActivityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CesiumActivity
        field = '__all__'
