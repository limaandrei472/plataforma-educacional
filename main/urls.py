from django.urls import path
from . import views

urlpatterns = [
    # --- FLUXO DE ENTRADA (Login e Cadastro) ---
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),

    path('inicio/', views.home, name='home'),
    path('perfil/', views.perfil_view, name='perfil_usuario'),
    path('professores/', views.professores_lista, name='professores_lista'),
    path('materia/<int:id_materia>/', views.materia_lista, name='materia_lista'),
    path('aula/<int:id_assunto>/', views.aula_detalhe, name='aula_detalhe'),
    path('professor/<int:id_professor>/', views.professor_perfil, name='professor_perfil'),
]