from rest_framework import generics
from .serializer import ProfilSerializer,CreateProfilSerializer
from .models import ProfilModel

from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

class CreateProfile(generics.CreateAPIView,CreateProfilSerializer):
    serializer_class = CreateProfilSerializer

    def get_queryset(self, *args, **kwargs):
        # Appel au custom_query_set() de la CreateProfilSerializer avec le super() helper
        return super().custom_query_set(self, *args, **kwargs)

    def create(user_data):
        #SEREALISATION
        return CreateProfilSerializer.custom_create(user_data)
    
class RetrieveProfil(generics.RetrieveAPIView):

    # ====== AUTHENTIFICATION ========#
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    lookup_field = 'user_id'
    
class UpdateProfile(generics.UpdateAPIView):

    # ====== AUTHENTIFICATION ========#
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    lookup_field = 'user_id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


