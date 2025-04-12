from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    pelicula = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='recetas/')
    ingredientes = models.TextField(help_text="Escribe cada ingrediente separado por una coma.")
    preparacion = models.TextField()
    destacada = models.BooleanField(default=False)  # Nuevo campo

    def lista_ingredientes(self):
        return [i.strip() for i in self.ingredientes.split(",") if i.strip()]

    def __str__(self):
        return self.titulo


class RecomendacionComida(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='recomendaciones/')
    ingredientes = models.TextField(help_text="Escribe cada ingrediente separado por una coma.")
    preparacion = models.TextField()

    def lista_ingredientes(self):
        return [i.strip() for i in self.ingredientes.split(",") if i.strip()]

    def __str__(self):
        return self.titulo

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.correo}"


class PoliticaPrivacidad(models.Model):
    titulo = models.CharField(max_length=200, default="Política de Privacidad")
    contenido = models.TextField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} ({self.fecha_actualizacion.strftime('%Y-%m-%d %H:%M')})"

CATEGORIAS = [
    ('cine', 'Cine'),
    ('recetas', 'Recetas'),
    ('decoracion', 'Decoración'),
    ('gastronomia', 'Gastronomía'),
]

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion_corta = models.TextField()
    contenido = models.TextField(help_text="Puedes usar HTML para resaltar frases, títulos, videos, etc.")
    imagen = models.ImageField(upload_to='noticias/')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(auto_now_add=True)
    tiempo_lectura = models.PositiveIntegerField(help_text="Tiempo estimado en minutos")
    slug = models.SlugField(unique=True, blank=True)
    video_url = models.URLField(blank=True, null=True, help_text="Enlace a un video relacionado (YouTube, etc.)")
    destacada = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
    

TIPO_ENLACE = [
    ('video', 'Video'),
    ('mapa', 'Mapa'),
    ('boton', 'Botón'),
]

class EnlaceInteres(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_ENLACE)
    embed_url = models.URLField(
    "Embed url", 
    blank=True, 
    null=True, 
    help_text="Solo para tipo Video o Mapa. Debe ser un enlace tipo 'embed'"
)
    texto_boton = models.CharField(max_length=100, blank=True)
    url_externa = models.URLField(blank=True)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.titulo} ({self.tipo})"

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='peliculas/')
    trailer_url = models.URLField(verbose_name="Enlace al tráiler")
    destacada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class IdeaDecoracion(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descripcion_corta = models.TextField()
    descripcion_larga = models.TextField()
    imagen_destacada = models.ImageField(upload_to='decoracion/')
    extras = models.TextField(blank=True, help_text="Consejos adicionales, separados por saltos de línea.")
    destacada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class FotoDecoracion(models.Model):
    idea = models.ForeignKey(IdeaDecoracion, related_name='fotos', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='decoracion/galeria/')
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Foto para {self.idea.titulo}"
    
class LandingPageConfig(models.Model):
    # Sección Hero
    titulo_hero = models.CharField(max_length=200, help_text="Título principal en la sección hero")
    descripcion_hero = models.TextField(help_text="Descripción en la sección hero")
    imagen_hero = models.ImageField(upload_to='landing/hero/', help_text="Fondo de la sección hero")

    # Sección Sobre el Proyecto
    titulo_sobre = models.CharField(max_length=200, default="Sobre el Proyecto")
    contenido_sobre = models.TextField(help_text="Descripción del proyecto")
    imagen_sobre = models.ImageField(upload_to='landing/sobre/', help_text="Imagen de acompañamiento")

    # Sección CTA (Llamado a la Acción)
    titulo_cta = models.CharField(max_length=200, help_text="Título del llamado a la acción")
    descripcion_cta = models.TextField(help_text="Descripción o invitación")
    texto_boton_cta = models.CharField(max_length=100, help_text="Texto del botón")
    enlace_boton_cta = models.URLField(help_text="Enlace que abre el botón")

    activo = models.BooleanField(default=True, help_text="Solo una configuración debe estar activa")

    def __str__(self):
        return "Configuración Landing Page Activa" if self.activo else "Configuración Landing Page (Inactiva)"


class FraseCinematografica(models.Model):
    frase = models.TextField(help_text="Texto de la frase")
    autor = models.CharField(max_length=100, help_text="Autor de la frase")
    activa = models.BooleanField(default=True, help_text="Solo una frase debe estar activa")

    def __str__(self):
        return f'"{self.frase[:30]}..." - {self.autor}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.noticia.titulo}"


class Comentario(models.Model):
    noticia = models.ForeignKey('Noticia', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} comentó en {self.noticia}"

class FavoritoPelicula(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos_peliculas')
    pelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE, related_name='favoritos')
    agregado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'pelicula')

    def __str__(self):
        return f"{self.usuario.email} → {self.pelicula.titulo}"

class FavoritoComida(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos_comidas')
    comida = models.ForeignKey('Receta', on_delete=models.CASCADE, related_name='favoritos')
    agregado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'comida')

    def __str__(self):
        return f"{self.usuario.email} → {self.comida.titulo}"
    
class FavoritoDecoracion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos_decoracion')
    decoracion = models.ForeignKey('IdeaDecoracion', on_delete=models.CASCADE, related_name='favoritos')
    agregado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'decoracion')

    def __str__(self):
        return f"{self.usuario.email} → {self.decoracion.titulo}"

class FavoritoNoticia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos_noticias')
    noticia = models.ForeignKey('Noticia', on_delete=models.CASCADE, related_name='favoritos')
    agregado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'noticia')

    def __str__(self):
        return f"{self.usuario.email} → {self.noticia.titulo}"
