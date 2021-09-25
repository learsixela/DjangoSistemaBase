from django.urls import path, include
from . import views

# todas las rutas de la app login estan incluidas en esta ruta
#  '' me redirige el view al metodo o funcion login
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('registrar', views.registrar),
    path('inicio', views.inicio),
    path('registro', views.registro),
    path('logout', views.logout),
]