from django.db import models

# Create your models here.

class Simulator(models.Model):
    localisation = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    delivery_point = models.CharField(max_length=200)
    delivery_delay = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.price