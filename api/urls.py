from django.urls import path
from api.apiviews import ProductoList, ProductoDetalle, SubCategoriaList, CategoriaList, CategoriaDetalle, SubCategoriaAdd, ProductoViewSet #CategoriaSave, SubCategoriaSave
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("v2/productos", ProductoViewSet, base_name="productos")

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<int:pk>/', ProductoDetalle.as_view(), name='producto_detalle'),
    path('v1/categorias/', CategoriaList.as_view(), name="categoria_save"),
    # path('v1/subcategorias/', SubCategoriaList.as_view(), name="subcategoria_save"),
    path('v1/categorias/<int:pk>/', CategoriaDetalle.as_view(), name="categoria_detalle"),
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(), name="sc_list"),
    path('v1/categorias/<int:cat_pk>/addsubcategoria/', SubCategoriaAdd.as_view(), name="sc_add"),
]

#Agregue lo que tiene mas la url que va generar
urlpatterns += router.urls
