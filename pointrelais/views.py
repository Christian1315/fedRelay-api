from rest_framework import generics
from .seriallizer import RelaySerializer

from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

class GetAllRelayPointForUser(generics.ListAPIView,RelaySerializer):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    lookup_field = "quartier_id"

    def get_queryset(self, *args, **kwargs):
        # Appel au custom_query_set() de la RelaySerializer avec le super() helper
        return super().custom_query_set(self, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        # Appel au custom_list() de la RelaySerializer avec le super() helper
        return super().custom_list(self, request, *args, **kwargs)

class GetAllRelayPoint(generics.ListAPIView,RelaySerializer):
    # === AUTHENTIFICATION ======#
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = RelaySerializer

    def get_queryset(self, *args, **kwargs):
        # Appel au getall() de la RelaySerializer avec le super() helper
        return super().getall(self, *args, **kwargs)
