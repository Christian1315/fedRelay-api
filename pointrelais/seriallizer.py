from rest_framework import serializers
from .models import Relaypoint
from rest_framework.response import Response

class RelaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Relaypoint
        fields = ["id","quartier_id","title","description","status","localisation","map_address"]


    def custom_query_set(self, *args, **kwargs):
        return Relaypoint.objects.all()

    def custom_list(self, request, *args, **kwargs):
        query = Relaypoint.objects.filter(quartier_id=kwargs["quartier_id"]).order_by('-id')
        serialisation = RelaySerializer(query,many=True).data

        return Response({'data':serialisation})

    def getall(self, *args, **kwargs):
        return Relaypoint.objects.all().order_by("-id")