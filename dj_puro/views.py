from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Categoria

# Create your views here.

def categoria_list(request):
    MAX_OBJECTS = 20
    # Devuelva todo los registros, con un máximo de 20
    cat = Categoria.objects.all()[:MAX_OBJECTS]
    # Crear un objeto json
    data = {"results": list(cat.values('descripcion', "activo"))}
    return JsonResponse(data)


def categoria_detalle(request, pk):
    cat = get_object_or_404(Categoria, pk=pk)
    data = {"results": {
        "descripcion": cat.descripcion,
        "activo": cat.activo
    }}
    return JsonResponse(data)
