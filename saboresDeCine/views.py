from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Pelicula, Receta, Noticia, PoliticaPrivacidad
from django.core.mail import send_mail
from .forms import MensajeContactoForm
from django.conf import settings
# Create your views here.

def mainPage(request):
    peliculas = Pelicula.objects.all()[:5]  # Carrusel
    recetas = Receta.objects.all()[:3]      # Recetas destacadas

    return render(request, 'index.html', {
        'peliculas': peliculas,
        'recetas': recetas,
    })

def comida(request):
    template = loader.get_template('comida.html')
    return HttpResponse(template.render())

def contacto(request):
    if request.method == 'POST':
        form = MensajeContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save()

            # Enviar correo
            send_mail(
                subject=f"Nuevo mensaje de {mensaje.nombre}",
                message=mensaje.mensaje,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            return render(request, 'contacto_exito.html', {'nombre': mensaje.nombre})
    else:
        form = MensajeContactoForm()

    return render(request, 'contacto.html', {'form': form})

def decoracion(request):
    template = loader.get_template('decoracion.html')
    return HttpResponse(template.render())

def enlaces(request):
    template = loader.get_template('enlaces.html')
    return HttpResponse(template.render())

def noticias(request):
    noticias = Noticia.objects.all().order_by('-id')
    return render(request, 'noticias.html', {'noticias': noticias})

def peliculas(request):
    template = loader.get_template('peliculas.html')
    return HttpResponse(template.render())

def privacidad(request):
    politica = PoliticaPrivacidad.objects.first()
    return render(request, 'privacidad.html', {'politica': politica})

def pelicula_detalle(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'pelicula_detalle.html', {'pelicula': pelicula})

def recetas_list(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas.html', {'recetas': recetas})

def receta_detalle(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'receta_detalle.html', {'receta': receta})

def modo_prueba(request):
    return render(request, 'modo_prueba.html')
