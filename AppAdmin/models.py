from django.db import models
from django.utils import timezone
from django.db import models
from typing import Any
from django.contrib.auth.models import AbstractUser, UserManager




## Cavalas (puestos)
class Cavalas(models.Model):
    idCavala = models.IntegerField(null=False, primary_key=True)
    sectorCavala = models.TextField(default="")
    estado = models.BooleanField(default=False)  # Estado (ocupado, desocupado)

    def __str__(self) -> str:
        return f"{self.sectorCavala} {self.idCavala}"





## User
class UserManager(UserManager):
    def create_user(self, rut, passwordLec=None, **extra_fields):
        if not rut:
            raise ValueError('El rut es obligatorio')

        # Asignamos el rut como username
        user = self.model(rut=rut, username=rut, **extra_fields)

        if passwordLec:
            user.set_password(passwordLec)

        user.save(using=self._db)
        return user
    
   



class User(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('admin', 'Administrador'),
        ('cliente', 'Cliente'),
        ('contador', 'Contador'),
        ('cabalero', 'Cabalero'),
    ]
    rut = models.CharField(unique=True, null=False, primary_key=True, max_length=12)
    nombres = models.CharField(max_length=40, default='')
    apellidos = models.CharField(max_length=40, default='')
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,   
    )
    telefono = models.PositiveBigIntegerField(blank=True, default=9)
    estado = models.BooleanField(default=False)
    direccion = models.TextField(blank=True, default='')

    objects = UserManager()


    def save(self, *args, **kwargs):
        # Asignamos rut a username y nombres, apellidos a first_name, last_name
        if not self.username:
            self.username = self.rut  # Asigna 'rut' al campo 'username'
        if not self.first_name:
            self.first_name = self.nombres  # Asigna 'nombres' a 'first_name'
        if not self.last_name:
            self.last_name = self.apellidos  # Asigna 'apellidos' a 'last_name'
        if self.password:  # Si la contraseña es nueva o modificada
            self.set_password(self.password)  # Cifra la contraseña antes de guardar
        if self.tipo_usuario == "contador" or self.tipo_usuario == 'cabalero' or self.tipo_usuario == 'admin':
            self.is_staff = True
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"
    


## Arriendos
class Arriendo(models.Model):
    id_arriendo = models.AutoField(primary_key=True)

    # Relación con el cliente y la cavala
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    cavala = models.ForeignKey(Cavalas, on_delete=models.CASCADE)
    
    # Campo de fecha y hora
    fecha_arriendo = models.DateTimeField(default=timezone.now)
    
    # Método de pago
    metodo_pago = models.BooleanField(default=False)  # True para pago efectivo, False para pago por internet
    estado = models.BooleanField(default=True)  # True = activo, False = terminado

    def __str__(self) -> str:
        return f"Arriendo de {self.cliente} en la cavala {self.cavala} - Fecha: {self.fecha_arriendo}"