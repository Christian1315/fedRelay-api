from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class ProfilModel(models.Model):
    nom = models.CharField(max_length=200,null=True)
    prenom = models.CharField(max_length=200,null=True)
    telephone = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    profession = models.CharField(max_length=200,null=True)
    pays = models.CharField(max_length=100,null=True)
    departement = models.CharField(max_length=100,null=True)
    commune = models.CharField(max_length=200,null=True)
    quartier = models.CharField(max_length=200,null=True)
    created_date = models.DateField(auto_now=True)
    avatar = models.CharField(max_length=10000,null=True)

    #==== RELATION ONE TO ONE ENTRE UN USER ET SON PROFIL =====#
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,unique=True)

    def __str__(self):
        return self.nom

