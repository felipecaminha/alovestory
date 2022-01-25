from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cursos', views.cursos, name='cursos'),
    path('sobre', views.sobre, name='sobre'),
    path('casos', views.casos, name='casos'),
    path('pesquisa', views.pesquisa, name='pesquisa'),
    path('ficha', views.ficha, name='ficha'),
    path('centros', views.centros, name='centros'),
    path('contato', views.contato, name='contato'),
]