from django.urls import path
from . import views

#aca estan las urls que se usaran en la aplicacion.

urlpatterns = [
    path('', views.index, name="index"),
    path('grass/', views.grass, name="grass"),
    path('flying/', views.flying, name="flying"),
    path('peso/', views.peso, name="peso"),
    path('invertidos/', views.invertidos, name="invertidos"),
    path('pokemones50/', views.pokemones50, name="pokemones50"),
]