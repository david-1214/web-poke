from django.contrib import admin
from . models import Pokemon

# Aca hicimos el registro de admin para la bbdd de pokemon que creamos con la pokeapi.


admin.site.register(Pokemon)