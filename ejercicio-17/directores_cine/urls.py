
from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('directores', views.listar_directores, name='directores'),
    path('nuevo-director', views.nuevo_director, name='nuevo-director'),
    path('editar-director/<int:id>', views.editar_director, name='editar-director'),
    path('eliminar-director/<int:id>',
         views.eliminar_director, name='eliminar-director'),
    path('peliculas', views.listar_peliculas, name='peliculas'),
    path('nuevo-pelicula', views.nueva_pelicula, name='nueva-pelicula'),
    path('editar-pelicula/<int:id>', views.editar_pelicula, name='editar-pelicula'),
    path('eliminar-pelicula/<int:id>',
         views.eliminar_pelicula, name='eliminar-pelicula'),
]
