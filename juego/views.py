

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

def rompecabezas(recuest):
	template = "juego/memorama.html