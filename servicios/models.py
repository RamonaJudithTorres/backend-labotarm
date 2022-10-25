from email.policy import default
from tokenize import blank_re
from django.db import models
from django.utils import timezone

# Create your models here.

# MODELO PACIENTE
class ModelPaciente(models.Model):
    nombre = models.CharField(max_length=200,null=False, blank=False)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.nombre}'

# MODELO ESTUDIO
class ModelEstudio(models.Model):
    nombre=models.CharField(max_length=200,null=False, blank=False)
    clave=models.CharField(max_length=200,null=False, blank=False)
    descripcion=models.TextField(null=True)


    def __str__(self):
        return f'{self.nombre}'      

# MODELO SERVICIO
class ModelServicio(models.Model):
    clave=models.CharField(max_length=200, blank=True, null=True)
    paciente =models.ForeignKey(ModelPaciente, on_delete=models.CASCADE, blank=True, null=True)
    costo=models.DecimalField(decimal_places=2, max_digits=7, default=0)
    resultado=models.TextField(null=True,blank=True, default='')
    fecha = models.DateTimeField(default= timezone.now)
    estudio =models.ManyToManyField(ModelEstudio)

    def __str__(self):
        return f'S. {self.clave}'   


# MODELO TARJETAS PAQUETES 
class Tarjetas(models.Model):
    nombre = models.CharField(max_length=200,null=False, blank=False)
    imagen=models.ImageField(upload_to='tarjeta', default='default.jpg')
    descripcion=models.TextField(null=True)

    def __str__(self):
        return f'{self.nombre}'  



