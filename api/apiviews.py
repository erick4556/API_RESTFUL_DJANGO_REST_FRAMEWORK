#from rest_framework.views import APIView
#from rest_framework.response import Response
#from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Producto, SubCategoria, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer, SubCategoriaSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import authenticate

from .permission import IsOwner

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


# Va trabajar igual tal cual como estaba antes
# USimplificando con vistas genéricas de DRF - Me muestra las propiedades de los campos
# ListCreateAPIView devuelve una lista de entidades o las crea, permite operaciones get y post
class ProductoList(generics.ListCreateAPIView):
    # Su tratamiento es queryset, se pueden filtrar, ordenar, se pueden segmentar como cualquier otra queryset
    queryset = Producto.objects.all()
    # Se utiliza para validar, deserealizar la entrada y también serealizar la salida
    serializer_class = ProductoSerializer


# Recupera los datos de una entidad o la elimina y permite get y delete
class ProductoDetalle(generics.RetrieveDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


# Permite crear entidades pero no las lista, permite post
class CategoriaSave(generics.CreateAPIView):
    serializer_class = CategoriaSerializer


class SubCategoriaSave(generics.CreateAPIView):
    serializer_class = SubCategoriaSerializer


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# class SubCategoriaList(generics.ListCreateAPIView):
#     queryset = SubCategoria.objects.all()
#     serializer_class = SubCategoriaSerializer

class SubCategoriaList(generics.ListCreateAPIView):
    # Filtrar subcategorias que pertenezcan a una categoria
    def get_queryset(self):
        # self.kwargs["pk"] : Lo que este en pk
        queryset = SubCategoria.objects.filter(categoria_id=self.kwargs["pk"])
        return queryset
    serializer_class = SubCategoriaSerializer


class CategoriaDetalle(generics.RetrieveDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class SubCategoriaAdd(APIView):
    def post(self, request, cat_pk):  # Sobrescribir el método post
        descripcion = request.data.get("descripcion")
        data = {"categoria": cat_pk, "descripcion": descripcion}
        serializer = SubCategoriaSerializer(data=data)
        if serializer.is_valid():
            subcat = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Imprimo los errores y devuelvo el status
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Ya el ViewSet me da los métodos POST, DELETE, PUT, GET, etc.


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    #Personalizar los permisos
    permission_class = [IsOwner] #Evaluar si es propietario


class UserCreate(generics.CreateAPIView):
    # Invalido IsAuthenticaded de settings para esta clase, inválido la configuración global de autenticación que es REST_FRAMEWORK de settings
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()  # No tome la configuración global para la autorización

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        # Verificar si la utenticación es correcta
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Credenciales incorrecta"}, status=status.HTTP_400_BAD_REQUEST)
