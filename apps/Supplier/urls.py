
from django.urls import path, re_path
from apps.Supplier.views import nuevoproveedor

app_name = 'Proveedores_app'
urlpatterns = [
    path('Nuevo_Proveedor', nuevoproveedor, name='nuevo_proveedor'),
]