from django.db import models

# Create your models here.
# aca cree la tabla que ocuparemos en esta app.
class Pokemon(models.Model):
    ID = models.CharField(max_length=200)
    Nombre = models.CharField(max_length=200)
    tipo1 = models.CharField(max_length=200)
    tipo2 = models.CharField(max_length=200)
    altura = models.CharField(max_length=200)
    peso = models.CharField(max_length=200)
    inv = models.CharField(max_length=200)

    def __str__(self):
        return self.Nombre