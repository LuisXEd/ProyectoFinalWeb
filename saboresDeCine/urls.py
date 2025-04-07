from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('noticias/', views.noticias, name='noticias'),
    path('decoracion/', views.decoracion, name='decoracion'),
    path('comida/', views.comida, name='comida'),
    path('enlaces/', views.enlaces, name='enlaces'),
    path('privacidad/', views.privacidad, name='privacidad'),
    path('recetas/', views.recetas_list, name='recetas_list'),
    path('recetas/<int:pk>/', views.receta_detalle, name='receta_detalle'),
    path('peliculas/<int:pk>/', views.pelicula_detalle, name='pelicula_detalle'),
]
