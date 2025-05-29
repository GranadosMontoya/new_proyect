from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import ProductsApi, CategoriaApi

router = DefaultRouter()
router.register('api/products', ProductsApi)
router.register('api/categorias', CategoriaApi)

urlpatterns = [
    path('', include(router.urls)), 
]