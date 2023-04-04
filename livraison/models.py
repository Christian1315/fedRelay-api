from django.db import models
# from django.contrib.auth.models import User
from api.settings import AUTH_USER_MODEL


# Create your models here.

class Delivery(models.Model):
    # ====  PREMIER FORMULAIRE =======#
    nomEmetteur = models.CharField(max_length=100)
    prenomEmetteur = models.CharField(max_length=100)
    telephoneEmetteur = models.CharField(max_length=100)
    emailEmetteur = models.CharField(max_length = 200)
    paysEmetteur = models.CharField(max_length = 200)

    departementEmetteur = models.CharField(max_length=100)
    communeEmetteur = models.CharField(max_length=100)
    quartierEmetteur = models.CharField(max_length=100)

    detailLocalisation = models.TextField(max_length=500)

    # ====  DEUXIEME FORMULAIRE =======#
    villeReception = models.CharField(max_length = 200)
    pointRelais = models.CharField(max_length = 200)
    notification = models.TextField(max_length = 500)

    # ====  TROIXIEME FORMULAIRE =======#
    nomDestinataire = models.CharField(max_length = 200)
    prenomDestinataire = models.CharField(max_length = 200)
    telephoneDestinataire = models.CharField(max_length = 200)
    emailDestinataire = models.EmailField()

    # ====  QUATRIEME FORMULAIRE ==== #
    typeColis = models.CharField(max_length = 200)
    poids = models.CharField(max_length = 200)
    description = models.TextField(max_length = 500)

    follow_code = models.CharField(max_length = 200,null=True)

    is_validated = models.BooleanField(default=False)
    transactionId = models.CharField(max_length=300,null=True,unique=True)

    is_lancement = models.BooleanField(default=True)
    is_enlevement = models.BooleanField(default=False)
    is_acheminement = models.BooleanField(default=False)
    is_reception = models.BooleanField(default=False)
    is_termine = models.BooleanField(default=False)

    # client_id = models.IntegerField()

    ##================= RELATION ENTRE LE USER ET LA LIVRAISON =============##

    user = models.IntegerField()

    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.nomEmetteur
        