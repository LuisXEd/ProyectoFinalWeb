from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='images/')
    fecha_estreno = models.DateField(null=True, blank=True)  # <-- Esto es esencial

    def __str__(self):
        return self.titulo


class Receta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    ingredientes = models.TextField()
    procedimiento = models.TextField()
    imagen = models.ImageField(upload_to='recetas/')
    peliculas = models.ManyToManyField(Pelicula, blank=True)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/')

    def __str__(self):
        return self.titulo

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"

