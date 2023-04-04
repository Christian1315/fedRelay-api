from .serializer import DeliverySerializer
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

# NB:: TOUTES LES CLASSES HERITENT DU DeliverySerializer
class GetAllDelivery(generics.ListAPIView,DeliverySerializer):

    # ====== AUTHENTIFICATION ========#
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # ====== APPEL AU SEREALISER_CLASS ========#
    serializer_class = DeliverySerializer

    # ====== Requete à la baSe de donnée ========#
    def get_queryset(self, *args, **kwargs):
        # Appel au custom_query_set() de la DeliverySerializer avec le super() helper
        return super().custom_query_set(self, *args, **kwargs)
    
    # ====== Retour de la liste des datas sérealisés ========#
    def list(self, *args, **kwargs):
        # Appel au custom_query_set() de la DeliverySerializer avec le super() helper
        return super().custom_list(self,*args, **kwargs)

class AddingOneDelivery(generics.CreateAPIView,DeliverySerializer):
   
    # ====== AUTHENTIFICATION ========#
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # ====== APPEL AU SEREALISER_CLASS ========#
    serializer_class = DeliverySerializer

    # ====== QuerySet ========#
    def get_queryset(self, *args, **kwargs):
        # Appel au query_set() de la DeliverySerializer avec le super() helper
        return super().query_set(self, *args, **kwargs)

    def create(self,request, *args, **kwargs):
        # Appel au custom_create() de la DeliverySerializer avec le super() helper
        return super().custom_create(request, *args, **kwargs)

class UpdateOneDelivery(generics.UpdateAPIView,DeliverySerializer):
    # ====== AUTHENTIFICATION ========#
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # ====== APPEL AU SEREALISER_CLASS ========#
    serializer_class = DeliverySerializer

    lookup_field = 'id'

    # ====== QuerySet ========#
    def get_queryset(self, *args, **kwargs):
        # Appel au query_set() de la DeliverySerializer avec le super() helper
        return super().query_set(self, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        # Appel au custom_update() de la DeliverySerializer avec le super() helper
        return super().custom_update(request, *args, **kwargs)

class FollowUpDelivery(generics.RetrieveAPIView,DeliverySerializer):
    # ====== AUTHENTIFICATION ========#
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # ====== APPEL AU SEREALISER_CLASS ========#
    serializer_class = DeliverySerializer

    lookup_field = 'follow_code'

    # ====== QuerySet ========#
    def get_queryset(self, *args, **kwargs):
        # Appel au query_set() de la DeliverySerializer avec le super() helper
        return super().query_set(self, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        # Appel au custom_update() de la DeliverySerializer avec le super() helper
        return super().custom_follow(self, request, *args, **kwargs)
        