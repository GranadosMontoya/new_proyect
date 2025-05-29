from rest_framework import serializers
from apps.Products.models import Producto,Categoria


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        extra_kwargs = {
            'sku': {'required': False, 'allow_null': True, 'allow_blank': True},
            'codigo_barras': {'required': False, 'allow_null': True, 'allow_blank': True},
            'imagen': {'required': False, 'allow_null': True},
            'fecha_vencimiento': {'required': False, 'allow_null': True},
            'motivo_actualizacion': {'required': False, 'allow_null': True, 'allow_blank': True},
            'usuario_ultimo_movimiento': {'required': False, 'allow_null': True},
        }


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']