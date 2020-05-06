

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

def tictactoe(request):
	template = "juego/gato.html"
	return render(request, template)

#def tictactoe(request):
 #   return render(request, 'gato.html')	

def simon(request):
	template = "juego/simondice.html"
	return render(request, template)		