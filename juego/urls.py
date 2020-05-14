from django.contrib import admin
from django.urls import include, path

# Views
from juego import views

app_name = "juego"
urlpatterns = [
path('space/', views.space, name = "space"),
path('tesoro/', views.tesoro, name = "tesoro"),
path('levels/', views.levels, name = "levels"),
<<<<<<< HEAD
path('rompecabezas/', views.rompecabezas, name = "rompecabezas"),
path('memorama/', views.memorama, name = "memorama"),
path('gato/', views.tictactoe, name = "gato"),
path('simon/', views.simon, name = "simon"),
path('encuentraCura/', views.encuentraCura, name = "encuentraCura"),
path('sopaDeLetras/', views.sopaLetras, name = "sopaDeLetras")
=======
path('gato/', views.tictactoe, name = "gato"),
path('simon/', views.simon, name = "simon"),
>>>>>>> 6a21ab1ffbae922553f3c2483a3429631d546481
]

