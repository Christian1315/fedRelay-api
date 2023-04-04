from rest_framework import serializers
from .models import Partenariat
from rest_framework.response import Response


class PartenariatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partenariat
        fields = ['nom','prenom','denomination','email','typ','object','lettre']

    def custom_query_set(self, *args, **kwargs):
        return Partenariat.objects.all()
    
    def partenariat_create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'success':True,'data':serializer.data}
        return Response(data)