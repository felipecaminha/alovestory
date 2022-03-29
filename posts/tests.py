from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
     path('<int:pk>/', views.detalhe_post, name='detalhe_post'),
]