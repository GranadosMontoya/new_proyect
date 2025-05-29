from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.Supplier.models import Proveedor
from .serializers import ProveedorSerializer

class ProveedoraApi(ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]  # Asegura que solo usuarios logueados accedan
