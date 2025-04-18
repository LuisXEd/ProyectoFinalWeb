# Generated by Django 5.2 on 2025-04-08 21:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EnlaceInteres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('tipo', models.CharField(choices=[('video', 'Video'), ('mapa', 'Mapa'), ('boton', 'Botón')], max_length=10)),
                ('embed_url', models.URLField(blank=True, help_text="Solo para tipo Video o Mapa. Debe ser un enlace tipo 'embed'", null=True, verbose_name='Embed url')),
                ('texto_boton', models.CharField(blank=True, max_length=100)),
                ('url_externa', models.URLField(blank=True)),
                ('orden', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FraseCinematografica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frase', models.TextField(help_text='Texto de la frase')),
                ('autor', models.CharField(help_text='Autor de la frase', max_length=100)),
                ('activa', models.BooleanField(default=True, help_text='Solo una frase debe estar activa')),
            ],
        ),
        migrations.CreateModel(
            name='IdeaDecoracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('descripcion_corta', models.TextField()),
                ('descripcion_larga', models.TextField()),
                ('imagen_destacada', models.ImageField(upload_to='decoracion/')),
                ('extras', models.TextField(blank=True, help_text='Consejos adicionales, separados por saltos de línea.')),
                ('destacada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LandingPageConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_hero', models.CharField(help_text='Título principal en la sección hero', max_length=200)),
                ('descripcion_hero', models.TextField(help_text='Descripción en la sección hero')),
                ('imagen_hero', models.ImageField(help_text='Fondo de la sección hero', upload_to='landing/hero/')),
                ('titulo_sobre', models.CharField(default='Sobre el Proyecto', max_length=200)),
                ('contenido_sobre', models.TextField(help_text='Descripción del proyecto')),
                ('imagen_sobre', models.ImageField(help_text='Imagen de acompañamiento', upload_to='landing/sobre/')),
                ('titulo_cta', models.CharField(help_text='Título del llamado a la acción', max_length=200)),
                ('descripcion_cta', models.TextField(help_text='Descripción o invitación')),
                ('texto_boton_cta', models.CharField(help_text='Texto del botón', max_length=100)),
                ('enlace_boton_cta', models.URLField(help_text='Enlace que abre el botón')),
                ('activo', models.BooleanField(default=True, help_text='Solo una configuración debe estar activa')),
            ],
        ),
        migrations.CreateModel(
            name='MensajeContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion_corta', models.TextField()),
                ('contenido', models.TextField(help_text='Puedes usar HTML para resaltar frases, títulos, videos, etc.')),
                ('imagen', models.ImageField(upload_to='noticias/')),
                ('categoria', models.CharField(choices=[('cine', 'Cine'), ('recetas', 'Recetas'), ('decoracion', 'Decoración'), ('gastronomia', 'Gastronomía')], max_length=20)),
                ('autor', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('tiempo_lectura', models.PositiveIntegerField(help_text='Tiempo estimado en minutos')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('video_url', models.URLField(blank=True, help_text='Enlace a un video relacionado (YouTube, etc.)', null=True)),
                ('destacada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='peliculas/')),
                ('trailer_url', models.URLField(verbose_name='Enlace al tráiler')),
                ('destacada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PoliticaPrivacidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='Política de Privacidad', max_length=200)),
                ('contenido', models.TextField()),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('pelicula', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='recetas/')),
                ('ingredientes', models.TextField(help_text='Escribe cada ingrediente separado por una coma.')),
                ('preparacion', models.TextField()),
                ('destacada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RecomendacionComida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='recomendaciones/')),
                ('ingredientes', models.TextField(help_text='Escribe cada ingrediente separado por una coma.')),
                ('preparacion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FotoDecoracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='decoracion/galeria/')),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='saboresDeCine.ideadecoracion')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saboresDeCine.noticia')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='saboresDeCine.noticia')),
            ],
        ),
    ]
