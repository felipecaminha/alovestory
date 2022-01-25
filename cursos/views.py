from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Curso


def cursos(request):
    cursos = Curso.objects.filter(data_publicacao__lte=timezone.now()).order_by('-data_publicacao') 
    return render(request, 'cursos/cursos.html', {'cursos': cursos})

def detalhe_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/detalhe_curso.html', {'curso': curso})