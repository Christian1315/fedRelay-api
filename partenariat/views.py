
from rest_framework import generics
from .serialize import PartenariatSerializer
from .models import Partenariat

from rest_framework.response import Response

# Create your views here.

class PartenariatRegister(generics.CreateAPIView):
    queryset = Partenariat.objects.all()
    serializer_class = PartenariatSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'success':True}
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data,headers=headers)
