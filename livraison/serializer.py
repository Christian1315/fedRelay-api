from rest_framework import serializers
from .models import Delivery
from rest_framework.response import Response

from api.customModule.mailModule import deliveryMail
from api.customModule.codeModule import getFollowCode

class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = (
        "id",
        "user",
        "nomEmetteur",
        "prenomEmetteur",
        "telephoneEmetteur",
        "emailEmetteur",
        "paysEmetteur",

        "departementEmetteur",
        "communeEmetteur",
        "quartierEmetteur",
        "detailLocalisation",

        "villeReception",
        "pointRelais",
        "notification",

        "nomDestinataire",
        "prenomDestinataire",
        "telephoneDestinataire",
        "emailDestinataire",

        "typeColis",
        "poids",
        "description",
        "follow_code",

        "is_validated",
        "transactionId",

        "is_lancement",
        "is_enlevement",
        "is_acheminement",
        "is_reception",
        "is_termine",

        "created_date",
        )
   
    #=========GENERALITES =============#    
    def query_set(self, *args, **kwargs):
        return Delivery.objects.all()
    
    # ============== METHODES RELATIVES AU GetAllDelivery CLASS ===========#
    def custom_query_set(self, *args, **kwargs):
        return Delivery.objects.filter(user=kwargs['user_id']).order_by('-id')
    
    def custom_list(self, *args, **kwargs):
        queryset = self.filter_queryset(self.custom_query_set(self, *args, **kwargs))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

    # ============== METHODES RELATIVES AU AddingOneDelivery CLASS ===========#

    def custom_create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data.get('user')
        colis_sender_email = request.user.phone_Or_email
        nomEmetteur = serializer.validated_data.get('nomEmetteur')
        prenomEmetteur = serializer.validated_data.get('prenomEmetteur')
        
        nomDestinataire = serializer.validated_data.get('nomDestinataire')
        prenomDestinataire = serializer.validated_data.get('prenomDestinataire')


        #### OBTENTION DU CODE DE SUIVI ####
        follow_code = getFollowCode(user_id) ### CODE DE SUIVI
        serializer.validated_data['follow_code']=follow_code

        #======= ENVOIE DE MAIL AU RECEIVER ======#
        deliveryMail(
            name=nomEmetteur + ' ' + prenomEmetteur,
            colis_sender_email=colis_sender_email,
            follow_code=follow_code,
            colis_recever_name=nomDestinataire + ' '+ prenomDestinataire,
            subject="Livraison sur FedRelay"
        )

        serializer.save()
        return Response({'success':True,'data':serializer.data})
    

    # ============== METHODES RELATIVES AU UpdateOneDelivery CLASS ===========#

    def custom_update(self, request, *args, **kwargs):

        is_delivery_exist = Delivery.objects.filter(id__exact = kwargs['id']).count()

        if is_delivery_exist==0:
            return Response({'success':False,'message':"Cette commande n'existe pas"})

        # VERIFIONS SI LA TRANSACTION EXISTE
        transactionId = request.POST.get('transactionId')
        delivery_count = Delivery.objects.filter(transactionId__exact = transactionId).count()

        if delivery_count!=0:
            return Response({'success':False,'message':'Cette transaction existe déjà'})

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"success":True,"data":serializer.data})

    # ============== METHODES RELATIVES AU FollowUpDelivery CLASS ===========#

    def custom_follow(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
                    'success':True,
                    'command_status':{
                        'is_validated':serializer.data['is_validated'],
                        'is_enlevement':serializer.data['is_enlevement'],
                        'is_acheminement':serializer.data['is_acheminement'],
                        'is_reception':serializer.data['is_reception'],
                        'is_termine':serializer.data['is_termine'],
                    }
                })

   