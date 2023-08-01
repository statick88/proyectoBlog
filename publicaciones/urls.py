# urls.py
from django.urls import path
from .views import lista_publicaciones, crear_publicacion, actualizar_publicacion, eliminar_publicacion, crear_comentario, lista_comentarios, actualizar_comentario, eliminar_comentario, detalle_publicacion, ListaPublicaciones, DetallePublicacion, ListaComentarios, DetalleComentario, home_view, contacto_view, quienes_somos_view, crear_view

urlpatterns = [
    # Rutas de Publicaciones
    path('', lista_publicaciones, name='lista_publicaciones'),
    path('lista/', lista_publicaciones, name='lista_publicaciones'),
    path('crear/', crear_publicacion, name='crear_publicacion'),
    path('detalle/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),
    path('actualizar/<int:pk>/', actualizar_publicacion, name='actualizar_publicacion'),
    path('eliminar/<int:pk>/', eliminar_publicacion, name='eliminar_publicacion'),
    
    # Rutas de Comentarios
    path('<int:pk>/actualizar_comentario/', actualizar_comentario, name='actualizar_comentario'),
    path('<int:pk>/eliminar_comentario/', eliminar_comentario, name='eliminar_comentario'),

    # Rutas de API
    path('publicaciones/', ListaPublicaciones.as_view(), name='lista_publicaciones'),
    path('publicaciones/<int:pk>/', DetallePublicacion.as_view(), name='detalle_publicacion'),
    path('comentarios/', ListaComentarios.as_view(), name='lista_comentarios'),
    path('comentarios/<int:pk>/', DetalleComentario.as_view(), name='detalle_comentario'),

    # Rutas de archivos estaticos
    path('home/', home_view, name='home'),
    path('contacto/', contacto_view, name='contacto'),
    path('quienes_somos/', quienes_somos_view, name='quienes_somos'),
    path('crear/', crear_view, name='crear_publicacion'),
    
    
]