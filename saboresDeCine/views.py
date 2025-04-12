from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from .forms import MensajeContactoForm
from .models import PoliticaPrivacidad, Noticia, EnlaceInteres, Pelicula, Receta, RecomendacionComida, IdeaDecoracion, LandingPageConfig, FraseCinematografica, FavoritoPelicula, FavoritoComida, FavoritoDecoracion, FavoritoNoticia
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm
from django.contrib import messages
from .forms import PerfilUsuarioForm, ComentarioForm
from .models import Like
from django.urls import reverse
from django.http import HttpResponseRedirect
import matplotlib.pyplot as plt
import io


@login_required
def perfil_usuario(request):
    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.', extra_tags='perfil')
            return redirect('perfil')
        else:
            messages.error(request, 'Revisa los campos. Hay un error.', extra_tags='perfil')
    else:
        form = PerfilUsuarioForm(instance=request.user)

    return render(request, 'perfil.html', {'form': form})

@login_required
def toggle_favorito_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    favorito, creado = FavoritoPelicula.objects.get_or_create(usuario=request.user, pelicula=pelicula)

    if not creado:
        favorito.delete() 
    return redirect('peliculas')  


@login_required
def dar_like(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)

    # Comprobamos si el usuario ya ha dado like
    if not Like.objects.filter(user=request.user, noticia=noticia).exists():
        Like.objects.create(user=request.user, noticia=noticia)

    # Redirigimos al detalle de la noticia
    return HttpResponseRedirect(reverse('noticia_detalle', args=[slug]))

def mainPage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente. ¡Ya puedes iniciar sesión!', extra_tags='registro')
            return redirect('login')
        else:
            messages.error(request, 'Hubo un error en el registro. Revisa los campos e intenta de nuevo.', extra_tags='registro')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})


def index(request):
    peliculas_destacadas = Pelicula.objects.filter(destacada=True)
    recetas_destacadas = Receta.objects.filter(destacada=True)
    ideas_destacadas = IdeaDecoracion.objects.filter(destacada=True)
    noticias_destacadas = Noticia.objects.filter(destacada=True)
    config = LandingPageConfig.objects.filter(activo=True).first()
    frases = FraseCinematografica.objects.filter(activa=True)

    return render(request, 'index.html', {
        'peliculas_destacadas': peliculas_destacadas,
        'recetas_destacadas': recetas_destacadas,
        'ideas_destacadas': ideas_destacadas,
        'noticias_destacadas': noticias_destacadas,
        'config': config,
        'frases': frases 
    })


def contacto(request):
    if request.method == 'POST':
        form = MensajeContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save()

            # Enviar correo
            send_mail(
                subject=f"Nuevo mensaje de {mensaje.nombre}",
                message=mensaje.mensaje,
                from_email=mensaje.correo,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Usa tu correo en settings
                fail_silently=False,
            )

            return render(request, 'contacto.html', {
                'form': MensajeContactoForm(),
                'mensaje_exito': True
            })
    else:
        form = MensajeContactoForm()
    
    return render(request, 'contacto.html', {'form': form})

@login_required
def toggle_favorito_decoracion(request, decoracion_id):
    idea = get_object_or_404(IdeaDecoracion, id=decoracion_id)
    favorito, creado = FavoritoDecoracion.objects.get_or_create(usuario=request.user, decoracion=idea)

    if not creado:
        favorito.delete()

    return redirect('decoracion')


def decoracion(request):
    query = request.GET.get('q', '')
    ideas = IdeaDecoracion.objects.all()
    favoritas = IdeaDecoracion.objects.filter(favoritos__usuario=request.user) if request.user.is_authenticated else IdeaDecoracion.objects.none()

    if query:
        ideas = ideas.filter(titulo__icontains=query) | ideas.filter(descripcion_corta__icontains=query)

    context = {
        'ideas': ideas,
        'favoritas': favoritas
    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('partials/lista_decoracion.html', context, request=request)
        return JsonResponse({'html': html})

    return render(request, 'decoracion.html', context)


def decoracion_detalle(request, slug):
    idea = get_object_or_404(IdeaDecoracion, slug=slug)
    extras = idea.extras.splitlines()
    return render(request, 'decoracion_detalle.html', {
        'idea': idea,
        'extras': extras
    })

def enlaces(request):
    enlaces = EnlaceInteres.objects.order_by('orden')
    return render(request, 'enlaces.html', {'enlaces': enlaces})


def noticias(request):
    buscar = request.GET.get('q', '')
    categoria = request.GET.get('categoria', '')

    noticias_qs = Noticia.objects.all()

    if buscar:
        noticias_qs = noticias_qs.filter(titulo__icontains=buscar)

    if categoria:
        noticias_qs = noticias_qs.filter(categoria=categoria)

    noticias_destacadas = Noticia.objects.filter(destacada=True)[:3]
    categorias = Noticia.objects.values_list('categoria', flat=True).distinct()

    favoritas = Noticia.objects.filter(favoritos__usuario=request.user) if request.user.is_authenticated else Noticia.objects.none()

    context = {
        'noticias': noticias_qs.order_by('-fecha_publicacion'),
        'noticias_destacadas': noticias_destacadas,
        'categorias': categorias,
        'categoria_seleccionada': categoria,
        'favoritas': favoritas,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('partials/lista_noticias.html', context, request=request)
        return JsonResponse({'html': html})

    return render(request, 'noticias.html', context)

@login_required
def dashboard(request):
    user = request.user

    total_peliculas = FavoritoPelicula.objects.filter(usuario=user).count()
    total_recetas = FavoritoComida.objects.filter(usuario=user).count()
    total_decoraciones = FavoritoDecoracion.objects.filter(usuario=user).count()
    total_noticias = FavoritoNoticia.objects.filter(usuario=user).count()

    context = {
        'total_peliculas': total_peliculas,
        'total_recetas': total_recetas,
        'total_decoraciones': total_decoraciones,
        'total_noticias': total_noticias,
    }

    return render(request, 'dashboard.html', context)


@login_required
def datos_dashboard(request):
    usuario = request.user
    datos = {
        "labels": ["Películas", "Recetas", "Decoración", "Noticias"],
        "valores": [
            FavoritoPelicula.objects.filter(usuario=usuario).count(),
            FavoritoComida.objects.filter(usuario=usuario).count(),
            FavoritoDecoracion.objects.filter(usuario=usuario).count(),
            FavoritoNoticia.objects.filter(usuario=usuario).count()
        ]
    }
    return JsonResponse(datos)


@login_required
def toggle_favorito_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    favorito, creado = FavoritoNoticia.objects.get_or_create(usuario=request.user, noticia=noticia)

    if not creado:
        favorito.delete()

    return redirect('noticias')




def peliculas(request):
    query = request.GET.get('q', '')
    peliculas_qs = Pelicula.objects.all()

    if query:
        peliculas_qs = peliculas_qs.filter(titulo__icontains=query)

    # 🔒 Solo mostramos los favoritos si el usuario está autenticado
    # ✅ Línea corregida (correcta)
    favoritos = Pelicula.objects.filter(favoritos__usuario=request.user) if request.user.is_authenticated else Pelicula.objects.none()

    context = {
        'peliculas': peliculas_qs,
        'favoritos': favoritos
    }

    # Depuración de AJAX
    print("⏺️ Cabecera:", request.headers.get('X-Requested-With'))
    print("⏺️ Es AJAX:", request.headers.get('X-Requested-With') == 'XMLHttpRequest')

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('partials/lista_peliculas.html', context, request=request)
        return JsonResponse({'html': html})

    return render(request, 'peliculas.html', context)




def privacidad(request):
    politica = PoliticaPrivacidad.objects.last()  # Obtener la última versión
    return render(request, 'privacidad.html', {'politica': politica})

def noticia_detalle(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    otras_noticias = Noticia.objects.exclude(slug=slug).order_by('-fecha_publicacion')[:5]

    like_count = Like.objects.filter(noticia=noticia).count()
    user_has_liked = request.user.is_authenticated and Like.objects.filter(user=request.user, noticia=noticia).exists()

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.noticia = noticia
            comentario.usuario = request.user
            comentario.save()
            return redirect('noticia_detalle', slug=slug)
    else:
        comentario_form = ComentarioForm()

    comentarios = noticia.comentarios.all()

    return render(request, 'noticias_detalle.html', {
        'noticia': noticia,
        'otras_noticias': otras_noticias,
        'comentarios': comentarios,
        'comentario_form': comentario_form,
        'like_count': like_count,
        'user_has_liked': user_has_liked,
    })




def comida(request):
    query = request.GET.get('q', '')
    recetas = Receta.objects.all()
    recomendaciones = RecomendacionComida.objects.all()

    if query:
        recetas = recetas.filter(titulo__icontains=query) | recetas.filter(pelicula__icontains=query)

    # Obtener recetas favoritas solo si está logueado
    recetas_favoritas = Receta.objects.filter(favoritos__usuario=request.user) if request.user.is_authenticated else Receta.objects.none()

    context = {
        'recetas': recetas,
        'recomendaciones': recomendaciones,
        'recetas_favoritas': recetas_favoritas
    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('partials/lista_recetas.html', context, request=request)
        return JsonResponse({'html': html})

    return render(request, 'comida.html', context)



@login_required
def toggle_favorito_comida(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    favorito, creado = FavoritoComida.objects.get_or_create(usuario=request.user, comida=receta)

    if not creado:
        favorito.delete()

    return redirect('comida')




def peliculas_destacadas(request):
    peliculas = Pelicula.objects.filter(destacada=True)
    return render(request, 'peliculas_destacadas.html', {'peliculas': peliculas})
