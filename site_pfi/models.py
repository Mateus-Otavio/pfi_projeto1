from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    matricula = models.CharField(max_length=30)
    curso = models.CharField(max_length=30)
    def __str__(self):
        return self.nome

class AlunoParticipa(models.Model):
    data_inicio = models.DateField()
    data_final = models.DateField(blank=True, null=True) #Estava dando erro, ver como deixar o campo não obrigatório
    carga_horaria_semanal = models.IntegerField()
    fk_atividade_extracurricualar = models.ForeignKey('AtividadeExtracurricular', on_delete=models.DO_NOTHING)
    fk_aluno = models.ForeignKey('Aluno', on_delete=models.DO_NOTHING)


class AtividadeExtracurricular(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField() #Talvez depois definir um numero maximo de caracterres
    tipo = models.CharField(max_length=50)
    situacao = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    docente = models.ForeignKey('Docente', on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.nome

# class Docente(User): #Continuar, comecei a usar o User
#     nome = models.CharField(max_length=50)
#     #email = models.EmailField(max_length=80)
#     formacao = models.CharField(max_length=80)
#     def __str__(self):
#         return self.nome
class Docente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    formacao = models.CharField(max_length=80)

    def email(self):
        return self.user.email

    def __str__(self):
        return self.nome

class Colaboradores(models.Model):
    data_inicio = models.DateField()
    data_final = models.DateField(blank=True, null=True)
    situacao = models.CharField(max_length=50)#Talvez usar o booleanfield
    fk_atividade_extracurricular = models.ForeignKey('AtividadeExtracurricular', on_delete=models.DO_NOTHING)
    fk_docente = models.ForeignKey('Docente', on_delete=models.CASCADE)

class Imagens(models.Model):
    descricao = models.TextField(blank=True, null=True)
    arquivo = models.ImageField()#Usar file ou binario
    extensao = models.CharField(max_length=10)
    fk_atividade_extracurricular = models.ForeignKey('AtividadeExtracurricular', on_delete=models.DO_NOTHING)

class Solicitacao(models.Model):
    data_solicitacao = models.DateField()
    situacao = models.BooleanField(default=False)
    fk_aluno = models.ForeignKey('Aluno', on_delete=models.DO_NOTHING)
    fk_atividade_extracurricular = models.ForeignKey('AtividadeExtracurricular', on_delete=models.DO_NOTHING)
