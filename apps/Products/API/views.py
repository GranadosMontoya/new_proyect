from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.Products.models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status
import traceback

class ProductsApi(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]  # Asegura que solo usuarios logueados accedan

    def perform_create(self, serializer):
        request_user = self.request.user
        serializer.save(usuario_ultimo_movimiento=request_user)

    def perform_update(self, serializer):
        request_user = self.request.user
        serializer.save(usuario_ultimo_movimiento=request_user)

    def create(self, request, *args, **kwargs):
        # Para depurar y controlar errores personalizados
        try:
            response = super().create(request, *args, **kwargs)
            return Response({
                'message': 'Producto creado exitosamente',
                'data': response.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Error al crear producto:")
            print(traceback.format_exc())
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response({
                'message': 'Producto actualizado exitosamente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class CategoriaApi(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer