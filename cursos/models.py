from django.conf import settings
from django.db import models
from django.utils import timezone


class Curso(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Autor")
    titulo = models.CharField(max_length=100, verbose_name="Título")
    subtitulo = models.CharField(max_length=200, verbose_name="Subtítulo")
    texto = models.TextField(verbose_name="Texto")
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name="Data de criação")
    data_publicacao = models.DateTimeField(blank=True, null=True, verbose_name="Data de publicação")

    def publish(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo