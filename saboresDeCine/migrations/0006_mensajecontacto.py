# Generated by Django 5.2 on 2025-04-07 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saboresDeCine', '0005_noticia'),
    ]

    operations = [
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
    ]
