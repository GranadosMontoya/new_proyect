from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)  # Nombre del contacto principal
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)  # Activo o Inactivo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
