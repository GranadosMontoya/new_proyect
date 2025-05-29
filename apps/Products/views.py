from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def NuevoProducto(request):
    return render(request, 'Products/nuevo_producto.html')