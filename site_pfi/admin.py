from django.contrib import admin

from site_pfi.models import Aluno, AlunoParticipa, AtividadeExtracurricular, Docente, Colaboradores, Imagens

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'matricula', 'curso')
    ordering = 'nome',

@admin.register(AlunoParticipa)
class AlunoParticipaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_inicio', 'data_final', 'carga_horaria_semanal', 'fk_atividade_extracurricualar', 'fk_aluno')
    ordering = 'id',

@admin.register(AtividadeExtracurricular)
class AtividadeExtracurricularAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_inicio', 'data_termino')
    ordering = 'nome',

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'formacao')
    ordering = 'nome',

@admin.register(Colaboradores)
class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_inicio', 'data_final', 'situacao', 'fk_atividade_extracurricular', 'fk_docente')


@admin.register(Imagens)
class ImagensAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'arquivo', 'extensao', 'fk_atividade_extracurricular')
    ordering = 'id',
