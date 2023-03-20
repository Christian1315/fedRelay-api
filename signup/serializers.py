from rest_framework import serializers
from django.contrib.auth.models import User

from .utils import sendEmailBox
from rest_framework.response import Response

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone_Or_email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone_Or_email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        #### ==== ENREGISTREMENT DU USER ===== ####
        user = User.objects.create_user(validated_data['username'], validated_data['phone_Or_email'], validated_data['password'])

        #======= ENVOIE DE MAIL AU RECEIVER ======#
        email = validated_data['phone_Or_email']

        subject = "Inscription sur FedRelay"
        template = 'signup_email.html'
        context = {
            'email':email,
        }
        receivers = [email]
        has_send = sendEmailBox(subject=subject,receivers=receivers,template=template,context=context)

        if has_send:
            print('envoyé avec succes!!')
        else:
            print("L'envoie de mail a échoué!!")
        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)