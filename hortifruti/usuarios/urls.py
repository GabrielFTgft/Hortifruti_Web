from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    # path('principal/', views.principal, name='principal'), # Página principal após login
    path('deslogar/', views.deslogar, name='deslogar'),
]
