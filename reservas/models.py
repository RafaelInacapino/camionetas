from django.db import models
from distutils.debug import DEBUG
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser,BaseUserManager

    

class Usuario(models.Model):
    rut = models.CharField(max_length=20, blank=True, primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=20, blank=True, null=True)
    apellido_materno = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.id_usuario+", "+self.rut+", "+self.nombre+", "+self.apellido_paterno+", "+self.apellido_materno+", "+self.fecha_nacimiento    

class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(db_column='id_vehiculo', primary_key=True)  
    patente = models.CharField(max_length=10, blank=True, null=True)
    marca = models.CharField(max_length=20,blank=True, null=True) 
    modelo = models.CharField(max_length=20,blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.id_vehiculo)+"," +self.patente+", "+self.marca+", "+self.modelo+", "+str(self.anio)
    
class Reserva_Inicial1(models.Model):
    motivo1 = models.CharField(max_length=60, blank=True,null=True)
    direccion1 = models.CharField(max_length=60, blank=True, null=True) 
    foto_tacometro1 = models.ImageField(upload_to='reservas/media', blank=True, null=True)
    
    def __str__(self):
        return self.motivo1+","+self.direccion1+","+self.foto_tacometro1.__str__()
    
class Reserva_Inicial2(models.Model):
    motivo2 = models.CharField(max_length=60, blank=True,null=True)
    direccion2 = models.CharField(max_length=60, blank=True, null=True) 
    foto_tacometro2 = models.ImageField(upload_to='reservas/media', blank=True, null=True)
    
    def __str__(self):
        return self.motivo2+","+self.direccion2+","+self.foto_tacometro2.__str__()
    
class Reserva_Final1(models.Model):
    observaciones1 = models.CharField(max_length=100, blank=True,null=True)
    foto_tacometro_final1 = models.ImageField(upload_to='reservas/media', blank=True, null=True)
    recarga_combustible1= models.ImageField(upload_to='reservas/media', blank=True, null=True)
    
    def __str__(self):
        return self.observaciones1+","+self.foto_tacometro_final1.__str__()+","+self.recarga_combustible1.__str__()
    
class Reserva_Final2(models.Model):
    observaciones2 = models.CharField(max_length=100, blank=True,null=True)
    foto_tacometro_final2 = models.ImageField(upload_to='reservas/media', blank=True, null=True)
    recarga_combustible2= models.ImageField(upload_to='reservas/media', blank=True, null=True)
    
    def __str__(self):
        return self.observaciones2+","+self.foto_tacometro_final2.__str__()+","+self.recarga_combustible2.__str__()