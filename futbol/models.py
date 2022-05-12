import datetime

from django.db import models

# Create your models here.
class Futbolista(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    nombre = models.TextField()
    equipo = models.TextField(max_length=150,default="pendiente")
    fecha_nacimiento = models.DateField()
    fecha_debut = models.DateField(default=None)
    equipo_debut = models.TextField(default=None)
    #imagen = models.ImageField(upload_to='image/imagejugador', default='*')


    def __str__(self):
        return self.nombre