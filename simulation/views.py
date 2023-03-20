from django.shortcuts import render
from rest_framework.response import Response

from django.http import JsonResponse

# Create your views here.
from rest_framework.decorators import api_view

from rest_framework import generics
from .serialize import SimulatorSerializer
from .models import Simulator

#CREATION DES SIMULATIONS
class SimulationCreate(generics.CreateAPIView):
    queryset = Simulator.objects.all()
    serializer_class = SimulatorSerializer

#RECUPERATION DU PRIX
@api_view(['POST'])
def SimulationResult(request):
    data = dict(request.data)
    form = SimulatorSerializer(data=data)

    if  form.is_valid():
        localisation = data['localisation']
        product_type = data['product_type']
        delivery_point = data['delivery_point']
        delivery_delay = data['delivery_delay']
        
        simulator_searched =  Simulator.objects.get(
            localisation=localisation,
            product_type=product_type,
            delivery_point=delivery_point,
            delivery_delay=delivery_delay
        )

        # RENVOIE DU PRIX
        return Response({'price':simulator_searched.price})
    else:
        return Response({'error':'Vos données ne sont pas valides'})