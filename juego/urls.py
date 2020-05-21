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
path('memorama/', views.memorama, name = "memorama"),
path('gato/', views.tictactoe, name = "gato"),
path('simon/', views.simon, name = "simon"),
path('encuentraCura/', views.encuentraCura, name = "encuentraCura"),
path('sopaDeLetras/', views.sopaLetras, name = "sopaDeLetras"),

path('gato/', views.tictactoe, name = "gato"),
path('simon/', views.simon, name = "simon"),
path('instruction/', views.inst, name = 'instruction'),
path('gatohist/', views.gatohist, name = 'gatohist'),
path('simonhist/', views.simonhist, name = 'simonhist'),
path('', views.home, name = 'index'),


]

