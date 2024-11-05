from django.db import models

class Asistente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    fecha_seminario = models.DateField()
    empresa = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.empresa}"


