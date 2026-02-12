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
        fields = ['id', 'nombre', 'descripcion']
        extra_kwargs = {
            'descripcion': {'required': False, 'allow_null': True, 'allow_blank': True}
        }
    
    def validate_nombre(self, value):
        # Normaliza el nombre a minúsculas
        value = value.lower().strip()
        
        # Verifica si ya existe una categoría con este nombre
        queryset = Categoria.objects.filter(nombre=value)
        
        if queryset.exists():
            raise serializers.ValidationError(
                f'Una categoría con el nombre "{value}" ya existe.'
            )
        
        return value