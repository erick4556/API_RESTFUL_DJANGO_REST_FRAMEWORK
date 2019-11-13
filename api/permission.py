from rest_framework import permission #Importo los permisos del rest_framework

class IsOwner(permission.BasePermission):
    message = "No es propietario bandido!!"

    # Sobreescribo el siguiente método
    def has_object_permission(self, request, view, obj):
        #Para que se pueda ver el contenido del app
        if request.method in permission.SAFE_METHODS #Si está en la lista de permisos ya sea get, options, head
            return True
        #Si es un método ya sea put, delete, post o patch, procede a hacer la comparación 
        return request.user == obj.owner #Si son iguales devuelve un true sino un false. Si el usuario es el propietario toma el owner