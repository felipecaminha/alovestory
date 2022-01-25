from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos, name='cursos'),
     path('<int:pk>/', views.detalhe_curso, name='detalhe_curso'),
]