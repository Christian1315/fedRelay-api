from django.db import models

# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField(max_length=300,unique=True)
    created_date = models.DateField(auto_now=True)


    def __str__(self):
        return self.email
    