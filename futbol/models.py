from django.db import models

# Create your models here.
class Futbolista(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    nombre = models.TextField()
    equipo = models.TextField(max_length=150,default="pendiente")
    fecha_nacimiento = models.DateField()


    def __str__(self):
        return self.nombre