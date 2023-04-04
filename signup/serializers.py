from rest_framework import serializers
from .models import MyUser

from api.customModule.mailModule import signUpMail

from profil.views import CreateProfile
from knox.models import AuthToken
from rest_framework.response import Response

from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from profil.models import ProfilModel
from django.contrib.auth import login
from django.forms.models import model_to_dict


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'phone_Or_email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'phone_Or_email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def query_set():
        return MyUser.objects.all()

    def custom_user_create(self,request):
        data = request.data

        #### ==== ENREGISTREMENT DU USER ===== ####
        user = MyUser.objects.create_user(
            username=data.get('username'),
            phone_Or_email=data.get('phone_Or_email'),
            password=data.get('password')
        )
        #### ==== CREATION DU PROFIL DU USER ===== ####
        user_data = UserSerializer(user, context=self.get_serializer_context()).data

        userProfil = CreateProfile.create(user_data)

        #======= ENVOIE DE MAIL AU RECEIVER ======#
        user_email = data.get('phone_Or_email')
        subject = "Inscription sur FedRelay"
        signUpMail(email=user_email,subject=subject)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "userProfil": userProfil
        })


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = MyUser
        fields = '__all__'

    def custom_login(request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        login(request, user)

        profil = ProfilModel.objects.get(user=user)
        userProfile =  model_to_dict(profil)
        return Response({
                "user": UserSerializer(user).data,
                "token": AuthToken.objects.create(user)[1],##Creation et récupération du Token user,
                "userProfile":userProfile
            })

class ChangePasswordSerializer(serializers.Serializer):
    class Meta:
        model = MyUser

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)