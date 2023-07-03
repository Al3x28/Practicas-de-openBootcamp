from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Director, Pelicula

class IndexView(generic.ListView):
    template_name = 'Peliculas/directores.html'
    model = Director

class DirectorView(generic.DetailView):
    template_name = 'Peliculas/director.html'
    model = Director

class PeliculaView(generic.DetailView):
    template_name = 'Peliculas/pelicula.html'
    model = Pelicula