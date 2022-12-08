from django.db import models


class Dispositivo(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.CharField('Estudiante', max_length=200)
    dni = models.IntegerField()

class Alerta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha de Alerta',null=False)
    iddispositivo = models.ForeignKey(Dispositivo,on_delete=models.CASCADE)

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    apellido = models.CharField('Apellidos', max_length=100)
    nombre = models.CharField('Nombres',max_length=100)
    dni = models.IntegerField()
    correo = models.CharField(max_length=200)
    iddispositivo = models.OneToOneField(Dispositivo,on_delete=models.CASCADE)