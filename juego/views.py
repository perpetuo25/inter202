

# Create your views here.
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required


@login_required(login_url='users:login')
def space(request):
    template = "juego/index.html"
    return render(request, template)
@login_required(login_url='users:login')
def tesoro(request):
	template = "juego/tesoro.html"
	return render(request, template)
@login_required(login_url='users:login')
def levels(request):
	template = "juego/levels.html"
	return render(request, template)

@login_required(login_url='users:login')
def rompecabezas(request):
	template = "juego/index2.html"
	return render(request, template)
@login_required(login_url='users:login')
def memorama(request):
	template = "juego/memorama.html"
	return render(request, template)

@login_required(login_url='users:login')
def tictactoe(request):
	template = "juego/gato.html"
	return render(request, template)

@login_required(login_url='users:login')
def simon(request):
	template = "juego/simondice.html"
	return render(request, template)
@login_required(login_url='users:login')
def encuentraCura(request):
	template = "juego/encuentraCura.html"
	return render(request, template)
@login_required(login_url='users:login')
def sopaLetras(request):
	template = "juego/sopaLetras.html"
	return render(request, template)
@login_required(login_url='users:login')
def inst(request):
	template = "juego/escrito.html"
	return render(request, template)
@login_required(login_url='users:login')
def wallyIntro(request):
	template = "juego/instruccionesWally.html"
	return render(request, template)
@login_required(login_url='users:login')
def letrasIntro(request):
	template = "juego/instruccionesSopaLetras.html"
	return render(request, template)

def home(request):
	template = "juego/home.html"
	return render(request, template)


		

