from rest_framework import generics
from .serialize import NewsletterSerializer

class EmailRegister(generics.CreateAPIView,NewsletterSerializer):
    serializer_class = NewsletterSerializer

    def get_queryset(self, *args, **kwargs):
        # Appel au custom_query_set() de la NewsletterSerializer avec le super() helper
        return super().custom_query_set(self, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # Appel au contact_create() de la ContactSerializer avec le super() helper
        return super().newsletter_create(request, *args, **kwargs)
