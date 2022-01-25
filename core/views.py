from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html', {})

def cursos(request):
    return render(request, 'core/cursos.html', {})

def sobre(request):
    return render(request, 'core/sobre.html', {})

def casos(request):
    return render(request, 'core/casos.html', {})

def pesquisa(request):
    return render(request, 'core/pesquisa.html', {})

def ficha(request):
    return render(request, 'core/ficha.html', {})

def centros(request):
    return render(request, 'core/centros.html', {})

def contato(request):
    return render(request, 'core/contato.html', {})