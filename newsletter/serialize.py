from rest_framework import serializers
from .models import Newsletter
from rest_framework.response import Response


import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['email']

    def custom_query_set(self, *args, **kwargs):
        return Newsletter.objects.all()

    def newsletter_create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #======= SETTING DU MAILCHIMP POUR ENVOIE DE MAIL =====#
        email = request.data['email']
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

        #======= ENREGISTREMENT DU MAIL DANS MAILCHIMP ======#
        try:
            mailchimp.lists.add_list_member(list_id, member_info)
        except ApiClientError as error:
            print("An exception occurred: {}".format(error.text))
        
        data = {'success':True,'data':serializer.data}
        return Response(data)