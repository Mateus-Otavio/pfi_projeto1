from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from site_pfi.models import Aluno, AtividadeExtracurricular, Imagens, AlunoParticipa, Colaboradores, Curso
from site_pfi.forms import AlunoForms, AtividadeForms, ImagensForms, AlunoParticipaForms, ColaboradoresForm, CursoForm


# def pagina_inicial(request):
#     return render(request, 'index.html')

# class IndexTemplateView(TemplateView):
#     template_name = "index.html" #Qual pagina vc quer que renderize

def exibir_ativi(request):
    return render(request, 'exibir_atividade.html')
def exibir_perfil(request):
    return render(request, 'perfil.html')

def exibir_form(request):
    return render(request, 'formulario_aluno_participa.html')
class AlunosListView(ListView):
    model = Aluno
    template_name = 'aluno_list.html'
    context_object_name = 'alunos' #Carrega uma lista com os dados do bd
    extra_context = {'form_titulo' : 'Lista de Alunos'}

class AlunoCreateView(CreateView):
    form_class = AlunoForms
    template_name = 'formulario.html' #Qual pagina ele vai carregar
    extra_context = {'form_titulo' : 'Cadastro Aluno'}
    success_url = reverse_lazy('alunos') #Quando der sucesso volta para a pagina de alunos

class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForms
    template_name = 'formulario.html'
    extra_context = {'form_titulo' : 'Editar Aluno'}
    success_url = reverse_lazy('alunos')

class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'excluir_registro.html'
    success_url = reverse_lazy('alunos')
    context_object_name = 'registro'
    extra_context = {'form_titulo': 'Deletar Aluno'}

#Parte das atividade extracurriculares
class AtividadeListView(ListView):
    model = AtividadeExtracurricular
    template_name = 'ativi_extracurriculares.html'
    form_class = AtividadeForms
    context_object_name = 'atividade_extracurricular'
    extra_context = {'form_titulo' : 'Lista de Atividades Extracurricular'}

class AtividadeCreateView(CreateView):
    form_class = AtividadeForms
    template_name = 'formulario.html'
    extra_context = {'form_titulo': 'Cadastro Atividade Extracurricular'}
    success_url = reverse_lazy('atividade_extracurricular')  # Quando der sucesso volta para a pagina de alunos

class AtividadeUpdateView(UpdateView):
    model = AtividadeExtracurricular
    form_class = AtividadeForms
    template_name = 'formulario.html'
    extra_context = {'form_titulo': 'Editar Atividade Extracurricular'}
    def get_success_url(self):
        # Usa 'reverse' para gerar a URL
        # 'exibir_atividade' é o nome da sua rota: name='exibir_atividade'
        # self.object.pk obtém o PK da atividade que acabou de ser atualizada
        return reverse('exibir_atividade', kwargs={'pk': self.object.pk}) # o metodo reverse possibilita que eu passe argumentos para a url

class AtividadeDeleteView(DeleteView):
    model = AtividadeExtracurricular
    template_name = 'excluir_registro.html'
    success_url = reverse_lazy('atividade_extracurricular')
    context_object_name = 'registro'
    extra_context = {'form_titulo': 'Deletar Atividade Extracurricular'}

#Parte das imagens

class ImagensListView(ListView):
    model = Imagens
    template_name = 'list_imagens.html'
    form_class = ImagensForms
    context_object_name = 'imagens'
    extra_context = {'form_titulo': 'Lista de Imagens'}

class ImagensCreateView(CreateView):
    form_class = ImagensForms
    template_name = 'formulario.html'
    extra_context = {'form_titulo': 'Cadastrar Imagem'}
    success_url = reverse_lazy('imagens')

class ImagensUpdateView(UpdateView):
    model = Imagens
    form_class = ImagensForms
    template_name = 'formulario.html'
    extra_context = {'form_titulo': 'Editar Imagem'}
    success_url = reverse_lazy('imagens')

class ImagensDeleteView(DeleteView):
    model = Imagens
    template_name = 'excluir_registro.html'
    success_url = reverse_lazy('imagens')
    context_object_name = 'registro'
    extra_context = {'form_titulo': 'Deletar Imagem'}

#Aluno participa

class AlunoParticipaListView(ListView):
    model = AlunoParticipa
    template_name = 'aluno_participa_list.html'
    form_class = AlunoParticipaForms
    context_object_name = 'participa_aluno'
    extra_context = {'form_titulo': 'Lista de Participação de todos os Alunos'}

class AlunoParticipaCreateView(CreateView):
    form_class = AlunoParticipaForms
    template_name = 'formulario.html'
    extra_context = {'form_titulo': 'Cadastro da participação de Alunos'}
    success_url = reverse_lazy('aluno_participa')

class AlunoParticipaUpdateView(UpdateView):
    model = AlunoParticipa
    form_class = AlunoParticipaForms
    template_name = 'formulario.html'
    extra_context = {'form_titulo': 'Editar participação do aluno'}
    success_url = reverse_lazy('aluno_participa')

class AlunoParticipaDeleteView(DeleteView):
    model = AlunoParticipa
    template_name = 'excluir_registro.html'
    success_url = reverse_lazy('aluno_participa')
    context_object_name = 'registro'
    extra_context = {'form_titulo': 'Deletar Particpação do aluno'}

#Colaboradores

class ColaboradoresListView(ListView):
    model = Colaboradores
    template_name = 'colaboradores_list.html'
    form_class = ColaboradoresForm
    context_object_name = 'colaboradores'
    extra_context = {'form_titulo': 'Lista de todos os Colaboradores'}

class ColaboradoresCreateView(CreateView):
    form_class = ColaboradoresForm
    template_name = 'formulario.html'
    extra_context = {'form_titulo': 'Cadastro de Colaboradores'}
    success_url = reverse_lazy('colaboradores')

class ColaboradoresUpdateView(UpdateView):
    model = Colaboradores
    form_class = ColaboradoresForm
    template_name = 'formulario.html'
    extra_context = {'form_titulo': 'Editar cadastro de Colaborador'}
    success_url = reverse_lazy('colaboradores')

class ColaboradoresDeleteView(DeleteView):
    model = Colaboradores
    template_name = 'excluir_registro.html'
    success_url = reverse_lazy('colaboradores')
    context_object_name = 'registro'
    extra_context = {'form_titulo': 'Deletar cadastro de colaborador'}

#Parte dos cursos
class CursoListView(ListView):
    model = Curso
    template_name = 'curso_list.html'
    form_class = CursoForm
    context_object_name = 'cursos'
    extra_context = {'form_titulo': 'Lista de todos os Cursos'}

class CursoCreateView(CreateView):
    form_class = CursoForm
    template_name = 'formulario.html'
    extra_context = {'form_titulo': 'Cadastro de Cursos'}
    success_url = reverse_lazy('cursos')

class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'formulario.html'
    extra_context = {'form_titulo': 'Editar Curso'}
    success_url = reverse_lazy('cursos')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'excluir_registro.html'
    success_url = reverse_lazy('cursos')
    context_object_name = 'registro'
    extra_context = {'form_titulo': 'Deletar Curso'}

def exibir_atividade(request, pk):
    atividade = AtividadeExtracurricular.objects.get(pk=pk)
    imagens = Imagens.objects.filter(fk_atividade_extracurricular=pk)

    context = {'atividade': atividade, 'imagens': imagens}
    return render(request,'exibir_atividade.html', context=context)

def listar_alunos_participando(request, pk):
    atividade = AtividadeExtracurricular.objects.get(pk=pk) #Pegando a pk que veio da url
    alunos_participando = AlunoParticipa.objects.filter(fk_atividade_extracurricualar=atividade) #Pegando o aluno de acordo com a atividade

    context = {
        'atividade': atividade,
        'alunos_participando': alunos_participando
    }
    return render(request, 'listar_alunos_participando.html', context=context)

def listar_colaboradores_participando(request, pk):
    atividade = AtividadeExtracurricular.objects.get(pk=pk) #Pegando a pk que veio da url
    colaboradores_participando = Colaboradores.objects.filter(fk_atividade_extracurricular=atividade) #Pegando o aluno de acordo com a atividade

    context = {
        'atividade': atividade,
        'colaboradores_participando': colaboradores_participando
    }
    return render(request, 'colaboradores_participando.html', context=context)

