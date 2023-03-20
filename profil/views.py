from django.shortcuts import render

from rest_framework import status
from rest_framework import generics
from .serializer import ProfilSerializer
from .models import ProfilModel
from rest_framework.response import Response

from knox.models import AuthToken

from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
# Create your views here.

# class CreateProfile(generics.CreateAPIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     queryset = ProfilModel.objects.all()
#     serializer_class = ProfilSerializer

#     def create(self, request,*args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         data = {'success':True}
#         # return Response(serializer.data, status=status.HTTP_201_CREATED,            headers=headers)
#         return Response(data,status=status.HTTP_201_CREATED,headers=headers)

class RetrieveProfil(generics.RetrieveAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    lookup_field = 'user_id'
    
class UpdateProfile(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    lookup_field = 'user_id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


