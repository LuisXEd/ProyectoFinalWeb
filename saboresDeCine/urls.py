from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('comida/', views.comida, name="comida"),
    path('receta/<int:receta_id>/favorito/', views.toggle_favorito_comida, name='toggle_favorito_comida'),
    path('contacto/', views.contacto, name="contacto"),
    path('decoracion/', views.decoracion, name="decoracion"),
    path('decoracion/<slug:slug>/', views.decoracion_detalle, name='decoracion_detalle'),
    path('decoracion/<int:decoracion_id>/favorito/', views.toggle_favorito_decoracion, name='toggle_favorito_decoracion'),
    path('enlaces/', views.enlaces, name="enlaces"),
    path('noticias/', views.noticias, name="noticias"),
    path('peliculas/', views.peliculas, name="peliculas"),
    path('pelicula/<int:pelicula_id>/favorito/', views.toggle_favorito_pelicula, name='toggle_favorito_pelicula'),
    path('privacidad', views.privacidad, name="privacidad"),
    path('noticias/<slug:slug>/', views.noticia_detalle, name="noticia_detalle"),
    path('noticia/<slug:slug>/like/', views.dar_like, name='dar_like'),
    path('noticia/<int:noticia_id>/favorito/', views.toggle_favorito_noticia, name='toggle_favorito_noticia'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/datos/', views.datos_dashboard, name='datos_dashboard'),



]