from rest_framework import serializers
from .models import Partenariat

class PartenariatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partenariat
        fields = ['nom','prenom','denomination','email','typ','object','lettre']