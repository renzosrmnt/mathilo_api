from django.urls import path,include
from rest_framework import routers

from . import views
from .api import UserViewSet
from .api import CategoriaViewSet
from .api import CarritoViewSet
from .api import ProductoViewSet
from .api import PedidoViewSet

router = routers.DefaultRouter()

router.register('api/user', UserViewSet, basename='mathilo')
router.register('api/categoria', CategoriaViewSet, basename='mathilo')
router.register('api/producto', ProductoViewSet, basename='mathilo')
router.register('api/carrito', CarritoViewSet, basename='mathilo')
router.register('api/pedido', PedidoViewSet, basename='mathilo')

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('categoria',views.CategoriaView.as_view()),
    path('producto',views.ProductoView.as_view()),
    path('user',views.UserView.as_view()),
    path('carrito',views.CarritoView.as_view()),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),
    path('producto/<int:producto_id>',views.ProductoDetailView.as_view()),
    path('user/<int:user_id>',views.UserDetailView.as_view()),
    path('carrito/<int:carrito_id>',views.CarritoDetailView.as_view()),
    path('admin/',include(router.urls))
] + router.urls