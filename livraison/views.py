from django.shortcuts import render
from django.http import JsonResponse

from django.forms.models import model_to_dict 
from .models import Delivery

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import DeliverySerializer

from rest_framework import generics,status

from datetime import datetime
from .utils import sendEmailBox

import random

from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
# Create your views here.

def Post_Delivry_Authentication(request,kwargs):
    ##MON CODE PERSONNALISE POUR VERIFIER SI LE USER EST CONNECTEE OU PAS##

    #Récupération du token envoyé par le client
    token_sent = kwargs['user_token']
    user_id = request.data['user']

    # print(user_id)
    
    #Recuperation des 8 premiers caractères du token envoyé par le client
    one = token_sent[0]
    two = token_sent[1]
    tree = token_sent[2]
    four = token_sent[3]
    five = token_sent[4]
    six = token_sent[5]
    seven = token_sent[6]
    eight = token_sent[7]
    
    #Formation du token de 8 caractères suivant le format qui se trouve dans la DB
    user_token_formed = one+two+tree+four+five+six+seven+eight

    #Verification de l'existance de ce token dans la DB
    is_user_authenticated = AuthToken.objects.filter(token_key=user_token_formed,user_id=user_id)

    #Action après vérification
    return is_user_authenticated

def Get_Delivry_Authentication(kwargs):
    ##MON CODE PERSONNALISE POUR VERIFIER SI LE USER EST CONNECTEE OU PAS##

    #Récupération du token envoyé par le client
    token_sent = kwargs['user_token']
    user_id = kwargs['user_id']

    # print(user_id)
    
    #Recuperation des 8 premiers caractères du token envoyé par le client
    one = token_sent[0]
    two = token_sent[1]
    tree = token_sent[2]
    four = token_sent[3]
    five = token_sent[4]
    six = token_sent[5]
    seven = token_sent[6]
    eight = token_sent[7]
    
    #Formation du token de 8 caractères suivant le format qui se trouve dans la DB
    user_token_formed = one+two+tree+four+five+six+seven+eight

    #Verification de l'existance de ce token dans la DB
    is_user_authenticated = AuthToken.objects.filter(token_key=user_token_formed,user_id=user_id)

    #Action après vérification
    return is_user_authenticated

class GetAllDelivery(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = DeliverySerializer

    def get_queryset(self, request, *args, **kwargs):
        return Delivery.objects.filter(user=kwargs['user_id']).order_by('-id')


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(self, request, *args, **kwargs))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AddingOneDelivery(generics.CreateAPIView):
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(request,serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'success':True}
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


    def perform_create(self,request,serializer):
        #======= ENVOIE DE MAIL AU RECEIVER ======#
        client_id = serializer.validated_data.get('client_id')
        sender_name = serializer.validated_data.get('nomEmetteur')
        sender_lastname = serializer.validated_data.get('prenomEmetteur')

        colis_sender_email = request.user.phone_Or_email
        colis_receiver_email = serializer.validated_data.get('emailDestinataire')
        nomDestinataire = serializer.validated_data.get('nomDestinataire')
        prenomDestinataire = serializer.validated_data.get('prenomDestinataire')

        nomEmetteur = serializer.validated_data.get('nomEmetteur')
        prenomEmetteur = serializer.validated_data.get('prenomEmetteur')

        # print(colis_sender_email)

        #### FORMATION DU CODE DE SUIVI ####
        list = ["A","B","C","D","E","F","G","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        letter_rand = random.choice(list)
        rand = random.randint(0,10000)

        # now = datetime.now()
        # timestamp = datetime.timestamp(now)
        # follow_code = "##"+str(timestamp) +"##" ### CODE DE SUIVI
        follow_code = "R"+str(client_id)+str(rand)+letter_rand ### CODE DE SUIVI

        serializer.validated_data['follow_code']=follow_code

        subject = "Livraison sur FedRelay"
        template = 'livraison_email.html'

        context = {
            'name':nomEmetteur + ' ' + prenomEmetteur,
            'date':datetime.today().date,
            'colis_recever_name':nomDestinataire + ' '+ prenomDestinataire,
            'follow_code':follow_code,
            'sender_name':sender_name,
            'sender_lastname':sender_lastname
        }
        
        receivers = [colis_sender_email]

        has_send = sendEmailBox(subject=subject,receivers=receivers,template=template,context=context)

        if has_send:
            serializer.save()
            print('envoyé avec succes!!')
        else:
            print('echoué avec succes!!')


class UpdateOneDelivery(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        transactionId = request.POST.get('transactionId')

        delivery_count = Delivery.objects.filter(transactionId__exact = transactionId).count()

        if delivery_count!=0:
            return Response({'success':False,'message':'Cette transaction existe déjà'})
        else:
            # print(kwargs['user_id'])
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)


class FollowUpDelivery(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    lookup_field = 'follow_code'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        if serializer.data:
            data = {
                        'success':True,
                        'command_status':serializer.data['status']
                    }

            return Response(data)
        return Response(serializer.data)