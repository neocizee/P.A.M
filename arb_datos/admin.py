from django.contrib import admin
from .models import Arbolado, Arbol_estado, Arbol_area_detalles, Arbol_especie, Vereda_estado

# Register your models here.

admin.site.register(Arbolado)
admin.site.register(Arbol_estado)
admin.site.register(Arbol_area_detalles)
admin.site.register(Vereda_estado)
admin.site.register(Arbol_especie)

