from django.shortcuts import render

from rest_framework import generics
from .serialize import NewsletterSerializer
from .models import Newsletter

from datetime import datetime
from .utils import sendEmailBox
from rest_framework.response import Response

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

from rest_framework import status

# Create your views here.

class EmailRegister(generics.CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'success':True}
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data,headers=headers)
# 

    def perform_create(self, serializer):
        email = serializer.validated_data.get('email')

        ### ENREGISTREMENT DU MAIL DANS LA DB ###
        serializer.save()


        #======= SETTING DU MAILCHIMP POUR ENVOIE DE MAIL =====#

        mailchimp = MailchimpMarketing.Client()

        mailchimp.set_config({
            "api_key": "080870593b957199a9e65a98f0468ba5-us14",
            "server": "us14"
        })

        list_id = "d5e394c3c4"

        member_info = {
            "email_address": email,
            "status": "subscribed",
            "merge_fields": {
            "FNAME": "",
            "LNAME": ""
            }
        }

        try:
            #======= ENREGISTREMENT DU MAIL DANS MAILCHIMP ======#
            response = mailchimp.lists.add_list_member(list_id, member_info)
            # print("response: {}".format(response))
        except ApiClientError as error:
            print("An exception occurred: {}".format(error.text))


        
        
