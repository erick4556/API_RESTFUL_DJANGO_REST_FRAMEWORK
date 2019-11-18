from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Producto, Categoria, SubCategoria
from rest_framework.authtoken.models import Token


class ProductoSerializer(serializers.ModelSerializer):
    # Para guardar el valor del usuario. Va ser un campo oculto
    # CurrentuserDefault valor que provee rest framework para obtener el usuario logueado
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Producto
        fields = '__all__'  # Le digo que voy a trabajar con todos los campos


class CategoriaSerializer(serializers.ModelSerializer):
     # Para guardar el valor del usuario. Va ser un campo oculto
    # CurrentuserDefault valor que provee rest framework para obtener el usuario logueado
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Categoria
        fields = '__all__'


class SubCategoriaSerializer(serializers.ModelSerializer):
     # Para guardar el valor del usuario. Va ser un campo oculto
    # CurrentuserDefault valor que provee rest framework para obtener el usuario logueado
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SubCategoria
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", 'email', 'password')  # Pasos que voy a usar
        # Especifico que no quiero que me devuelva la contraseña en el response
        extra_kwargs = {'password': {'write_only': True}}

    # Sobreescribir el método create
    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    username=validated_data['username'])  # Lo que se envía como parámetro
        # Me aseguro que la contraseña se guarde bien
        user.set_password(validated_data['password'])
        user.save()  # Guardo el usuario
        Token.objects.create(user=user)  # Creo el token y asigno el usuario
        return user  # Retorno el usuario que se guardó
