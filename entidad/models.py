from django.db import models

# Create your models here.
class Pentidad(models.Model):
    nombre = models.CharField(max_length=255)
