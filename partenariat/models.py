from django.db import models

# Create your models here.

class Partenariat(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    denomination = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    typ = models.CharField(max_length=200)

    object = models.CharField(max_length=200)
    lettre = models.CharField(max_length=500)
    created_date = models.DateField(auto_now=True)


    def __str__(self):
        return self.nom


