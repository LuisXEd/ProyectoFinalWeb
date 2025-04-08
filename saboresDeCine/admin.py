from django.contrib import admin
from .models import Pelicula, Receta, Noticia, PoliticaPrivacidad

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_estreno')
    search_fields = ('titulo',)

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    filter_horizontal = ('peliculas',)

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

@admin.register(PoliticaPrivacidad)
class PoliticaPrivacidadAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

    def has_add_permission(self, request):
        # Evita que se creen más de una política
        if PoliticaPrivacidad.objects.exists():
            return False
        return super().has_add_permission(request)
