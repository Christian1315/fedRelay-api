
from rest_framework import generics
from .serialize import PartenariatSerializer
from .models import Partenariat

from rest_framework.response import Response

# Create your views here.

class PartenariatRegister(generics.CreateAPIView,PartenariatSerializer):
    serializer_class = PartenariatSerializer

    def get_queryset(self, *args, **kwargs):
        # Appel au custom_query_set() de la PartenariatSerializer avec le super() helper
        return super().custom_query_set(self, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().partenariat_create(request, *args, **kwargs)
