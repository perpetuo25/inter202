from django.contrib import admin
from django.urls import include, path

# Views
from juego import views

app_name = "juego"
urlpatterns = [
path('space/', views.space, name = "space"),
path('tesoro/', views.tesoro, name = "tesoro"),
path('levels/', views.levels, name = "levels"),
path('rompecabezas/', views.rompecabezas, name = "rompecabezas"),
]

