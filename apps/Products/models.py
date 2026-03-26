from django.db import models
from apps.User.models import User
from apps.Supplier.models import Proveedor
import uuid

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        # Normalizar el nombre a minúsculas para evitar duplicados
        self.nombre = self.nombre.lower().strip()
        super().save(*args, **kwargs)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    sku = models.CharField(max_length=20, unique=True, blank=True, null=True)
    codigo_barras = models.CharField(max_length=50, unique=True)
    imagen = models.ImageField(upload_to='products', height_field=None, width_field=None, max_length=None, blank=True , default='logos/default-img.jpg')
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    precio_publico = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=20, choices=[('kg', 'Kilogramos'), ('lt', 'Litros'), ('unidad', 'Unidad')])
    perecedero = models.BooleanField(default=True)
    impuesto = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    estado = models.CharField(
        max_length=20,
        choices=[('activo', 'Activo'), ('agotado', 'Agotado'), ('descontinuado', 'Descontinuado')],
        default='activo'
    )
    motivo_actualizacion = models.TextField(blank=True, null=True)

    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    usuario_ultimo_movimiento = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def margen_ganancia(self):
        return self.precio_publico - self.precio_base

    def porcentaje_ganancia(self):
        if self.precio_base > 0:
            return (self.margen_ganancia() / self.precio_base) * 100
        return 0

    def generar_sku(self):
        if self.codigo_barras:
            return self.codigo_barras[:8]  # Tomar los primeros 8 caracteres del código de barras
        return f"{self.categoria.nombre[:3].upper()}-{uuid.uuid4().hex[:5].upper()}"  # Generar un código único

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generar_sku()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sku} - {self.nombre}"
