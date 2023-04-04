
from rest_framework import generics
from .serialize import ContactSerializer
from .models import Contact

from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ContactRegister(generics.CreateAPIView,ContactSerializer):
    serializer_class = ContactSerializer

    def get_queryset(self, *args, **kwargs):
        # Appel au custom_query_set() de la ContactSerializer avec le super() helper
        return super().custom_query_set(self, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # Appel au contact_create() de la ContactSerializer avec le super() helper
        return super().contact_create(request, *args, **kwargs)
        


    