from rest_framework import serializers
from .models import Simulator

class SimulatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulator
        fields = ("localisation","product_type","delivery_point","delivery_delay")