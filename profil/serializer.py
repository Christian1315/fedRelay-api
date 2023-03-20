from rest_framework import serializers
from .models import ProfilModel

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfilModel
        fields = ['nom','prenom','telephone','email','profession','pays','ville','quartier','avatar','user']