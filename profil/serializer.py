from rest_framework import serializers
from .models import ProfilModel
from django.forms.models import model_to_dict
from signup.models import MyUser


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfilModel
        fields = '__all__'


class CreateProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfilModel
        fields = ('telephone','email','user')

    def custom_query_set(self, *args, **kwargs):
        return ProfilModel.objects.all()
    
    def custom_create(user_data):
        user = MyUser.objects.get(id=user_data['id'])

        phone_Or_email = user_data['phone_Or_email']
        liste = phone_Or_email.split('@')

        ## VERIFIONS S'IL S'AGIT D'UN MAIL OU D'UN PHONE
        if len(liste)==2: ##C'est un mail
            email = phone_Or_email
            telephone = ""
        else: ## C'est un phone
            telephone = phone_Or_email
            email = ""

        profil = ProfilModel.objects.create(user=user,nom='',prenom='',telephone=telephone,email=email,profession='',pays='',departement='',commune='',quartier='',avatar='')
        return model_to_dict(profil)
