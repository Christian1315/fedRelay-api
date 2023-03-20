
from rest_framework import generics
from .serialize import ContactSerializer
from .models import Contact

from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ContactRegister(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'success':True}
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


    