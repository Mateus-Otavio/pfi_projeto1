"""pfi_projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from site_pfi import views
from site_pfi.views import (AlunosListView, AlunoCreateView, AlunoUpdateView,
                            AlunoDeleteView, AtividadeListView, AtividadeCreateView, AtividadeUpdateView,
                            AtividadeDeleteView, ImagensListView, ImagensCreateView, ImagensUpdateView,
                            ImagensDeleteView, AlunoParticipaListView, AlunoParticipaCreateView,
                            AlunoParticipaUpdateView, AlunoParticipaDeleteView, ColaboradoresListView,
                            ColaboradoresCreateView, ColaboradoresUpdateView, ColaboradoresDeleteView, exibir_ativi,
                            exibir_perfil, exibir_form, CursoListView, CursoCreateView, CursoUpdateView, CursoDeleteView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AtividadeListView.as_view(), name='atividade_extracurricular'),
    path('exibir_perfil/', views.exibir_perfil, name='exibir_perfil'),
    # path('', IndexTemplateView.as_view(),  name='home'),
     path('aluno_form/', views.exibir_form, name='aluno_form'),
    path('exibir_ativi/<int:pk>', views.exibir_atividade, name='exibir_atividade'),
    path('atividade/<int:pk>/alunos/', views.listar_alunos_participando, name='listar_alunos_participando'),
    path('atividade/<int:pk>/colaboradores/', views.listar_colaboradores_participando, name='listar_colaboradores_participando'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html', next_page='atividade_extracurricular'), name='logout'),
    path('alunos/', AlunosListView.as_view(), name='alunos'),
    path('add_alunos/', AlunoCreateView.as_view(),  name='novo_aluno'),
    path('edit_aluno/<int:pk>/', AlunoUpdateView.as_view(), name='editar_aluno'),
    path('remover_aluno/<int:pk>/', AlunoDeleteView.as_view(), name='remover_aluno' ),
    #Parte de rotas Atividades extracurriculares

    path('add_atividade/', AtividadeCreateView.as_view(),  name='nova_atividade'),
    path('edit_atividade/<int:pk>/', AtividadeUpdateView.as_view(), name='editar_atividade'),
    path('remover_atividade_extracurricular/<int:pk>/', AtividadeDeleteView.as_view(), name='remover_atividade'),

#Parte das Imagens
    path('imagens/', ImagensListView.as_view(), name='imagens'),
    path('add_imagens/', ImagensCreateView.as_view(), name='adicionar_imagens'),
    path('edit_imagem/<int:pk>/', ImagensUpdateView.as_view(), name='editar_imagem'),
    path('remover_imagem/<int:pk>/', ImagensDeleteView.as_view(), name='remover_imagem'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

#Parte do aluno participa
    path('aluno_participa/', AlunoParticipaListView.as_view(), name='aluno_participa'),
    path('add_partici_aluno', AlunoParticipaCreateView.as_view(), name='nova_participacao'),
    path('edit_parti_aluno/<int:pk>', AlunoParticipaUpdateView.as_view(), name='editar_paticipacao'),
    path('remover_participacao_aluno/<int:pk>', AlunoParticipaDeleteView.as_view(), name='remover_participacao'),

#Parte dos colaboradores
    path('colaboradores/', ColaboradoresListView.as_view(), name='colaboradores'),
    path('add_colaborador/', ColaboradoresCreateView.as_view(), name='novo_colaborador'),
    path('edit_colaborador<int:pk>', ColaboradoresUpdateView.as_view(), name='editar_colaborador'),
    path('remover_colaborador/<int:pk>', ColaboradoresDeleteView.as_view(), name='remover_colaborador'),

#Parte dos cusos
    path('cursos/', CursoListView.as_view(), name='cursos'),
    path('add_curso/', CursoCreateView.as_view(), name='novo_curso'),
    path('edit_curso/<int:pk>/', CursoUpdateView.as_view(), name='editar_curso'),
    path('remover_curso/<int:pk>/', CursoDeleteView.as_view(), name='remover_curso'),

]



