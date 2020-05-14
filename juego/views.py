

# Create your views here.
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views import View


def space(request):
    template = "juego/index.html"
    return render(request, template)

def tesoro(request):
	template = "juego/tesoro.html"
	return render(request, template)

def levels(request):
	template = "juego/levels.html"
	return render(request, template)


def rompecabezas(request):
	template = "juego/index2.html"
	return render(request, template)

def memorama(request):
	template = "juego/memorama.html"
	return render(request, template)


def tictactoe(request):
	template = "juego/gato.html"
	return render(request, template)


def simon(request):
	template = "juego/simondice.html"
	return render(request, template)

def encuentraCura(request):
	template = "juego/encuentraCura.html"
	return render(request, template)

def sopaLetras(request):
	template = "juego/sopaLetras.html"
	return render(request, template)

# #def tictactoe(request):
#     return render(request, 'gato.html')	

# def simon(request):
# 	template = "juego/simondice.html"
# 	return render(request, template)		

