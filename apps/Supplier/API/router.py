from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import ProveedoraApi

router = DefaultRouter()
router.register('api/proveedor', ProveedoraApi)

urlpatterns = [
    path('', include(router.urls)), 
]