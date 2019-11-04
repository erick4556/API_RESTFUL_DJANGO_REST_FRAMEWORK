#from rest_framework.views import APIView
#from rest_framework.response import Response
#from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Producto, SubCategoria, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer, SubCategoriaSerializer


""" class ProductoList(APIView):
    def get(self, request):
        # Devolver todos los productos, 20 registros se devuelven
        prod = Producto.objects.all()[:20]
        data = ProductoSerializer(prod, many=True).data #Devuelve varios registros
        return Response(data)


class ProductoDetalle(APIView):
    def get(self,request, pk):
        prod = get_object_or_404(Producto, pk=pk)
        data = ProductoSerializer(prod).data
        return Response(data)
         """


#Va trabajar igual tal cual como estaba antes
#USimplificando con vistas genéricas de DRF - Me muestra las propiedades de los campos
class ProductoList(generics.ListCreateAPIView): #ListCreateAPIView devuelve una lista de entidades o las crea, permite operaciones get y post
    queryset = Producto.objects.all() #Su tratamiento es queryset, se pueden filtrar, ordenar, se pueden segmentar como cualquier otra queryset
    serializer_class = ProductoSerializer #Se utiliza para validar, deserealizar la entrada y también serealizar la salida
 
 
class ProductoDetalle(generics.RetrieveDestroyAPIView): #Recupera los datos de una entidad o la elimina y permite get y delete
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CategoriaSave(generics.CreateAPIView): #Permite crear entidades pero no las lista, permite post
    serializer_class = CategoriaSerializer

class SubCategoriaSave(generics.CreateAPIView):
    serializer_class = SubCategoriaSerializer


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class SubCategoriaList(generics.ListCreateAPIView):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializer    




