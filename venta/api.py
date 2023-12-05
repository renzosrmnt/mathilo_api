from venta.models import *
from rest_framework import viewsets, permissions
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = UserSerializer
  
class CategoriaViewSet(viewsets.ModelViewSet):
  queryset = Categoria.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = CategoriaSerializer
  
class ProductoViewSet(viewsets.ModelViewSet):
  queryset = Producto.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = ProductoSerializer
  
class CarritoViewSet(viewsets.ModelViewSet):
  queryset = Carrito.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = CarritoSerializer 
  
class PedidoViewSet(viewsets.ModelViewSet):
  queryset = PedidoPersonalizado.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = PedidoSerializer