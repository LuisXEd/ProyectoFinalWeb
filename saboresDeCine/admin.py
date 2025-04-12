from django.contrib import admin
from .models import PoliticaPrivacidad, Noticia, EnlaceInteres, Pelicula, Receta, RecomendacionComida, IdeaDecoracion, FotoDecoracion, LandingPageConfig, FraseCinematografica, Comentario


admin.site.register(PoliticaPrivacidad)

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pelicula', 'destacada')
    list_filter = ('destacada',)
    search_fields = ('titulo', 'pelicula')


admin.site.register(RecomendacionComida)

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'fecha_publicacion', 'tiempo_lectura', 'destacada')  
    list_filter = ('categoria', 'fecha_publicacion', 'destacada')  
    search_fields = ('titulo', 'descripcion_corta', 'contenido', 'autor')
    prepopulated_fields = {"slug": ("titulo",)}
    readonly_fields = ('fecha_publicacion',)

    fieldsets = (
        (None, {
            'fields': ('titulo', 'slug', 'descripcion_corta', 'contenido', 'imagen', 'destacada')  
        }),
        ('Metadatos', {
            'fields': ('categoria', 'autor', 'tiempo_lectura', 'video_url')
        }),
    )


@admin.register(EnlaceInteres)
class EnlaceInteresAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'orden')
    list_filter = ('tipo',)
    ordering = ('orden',)

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    list_filter = ('destacada',)
    search_fields = ('titulo',)

class FotoDecoracionInline(admin.TabularInline):
    model = FotoDecoracion
    extra = 1

@admin.register(IdeaDecoracion)
class IdeaDecoracionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'destacada')  
    prepopulated_fields = {"slug": ("titulo",)}
    inlines = [FotoDecoracionInline]

@admin.register(LandingPageConfig)
class LandingPageConfigAdmin(admin.ModelAdmin):
    list_display = ('titulo_hero', 'activo')
    list_filter = ('activo',)

@admin.register(FraseCinematografica)
class FraseCinematograficaAdmin(admin.ModelAdmin):
    list_display = ('frase', 'autor', 'activa')
    list_filter = ('activa',)

admin.site.register(Comentario)