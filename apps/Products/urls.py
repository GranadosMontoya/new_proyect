
from django.urls import path, re_path
from apps.Products.views import NuevoProducto

app_name = 'Productos_app'
urlpatterns = [
    path('Nuevo_Producto', NuevoProducto, name='nuevo_producto'),
]
 
