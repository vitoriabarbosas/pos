from django.db import models

# Create your models here.

class Incidents(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    number_pedido = models.TextField(max_length=255)
    assunto = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    
    