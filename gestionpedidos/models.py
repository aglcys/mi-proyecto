from django.db import models

class Empleado(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    tlfno=models.CharField(max_length=20)

class Implementos(models.Model):
    nombre=models.CharField(max_length=30)
    categoria=models.CharField(max_length=30)
    cantidad=models.CharField(max_length=30)

class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
