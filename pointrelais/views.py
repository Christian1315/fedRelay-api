from django.shortcuts import render
from rest_framework import generics
from .models import Relaypoint
from .seriallizer import RelaySerializer

from rest_framework.response import Response

from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

# Create your views here.

class GetAllRelayPointForUser(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    lookup_field = "quartier_id"

    def list(self, request, *args, **kwargs):
        
        query = Relaypoint.objects.filter(quartier_id=kwargs["quartier_id"]).order_by('-id')
        serialisation = RelaySerializer(query,many=True).data

        return Response({'data':serialisation})


class GetAllRelayPoint(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Relaypoint.objects.all().order_by("-id")
    serializer_class = RelaySerializer