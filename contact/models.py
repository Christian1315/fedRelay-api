from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    message = models.CharField(max_length=600)
    object = models.CharField(max_length=600)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom