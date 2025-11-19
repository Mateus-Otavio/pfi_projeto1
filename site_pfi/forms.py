from random import choices

from django import forms
from site_pfi.models import Aluno, AtividadeExtracurricular, Imagens, AlunoParticipa, Colaboradores, Curso

#Model é onde pegamos os dados do models e tambem formatamos o formulario

class AlunoForms(forms.ModelForm):
    class Meta:
        model = Aluno  # classe de modelo (criada no models)
        fields = '__all__'
        # exclude = ["ativo"]  # campos que não serão exibidos
        labels = {'nome': 'Nome do Aluno'}  # configura o texto do label
        widgets = {
            'nome': forms.TextInput(attrs= #A ordem dos campos pode seer facilmente mudada pela ordem dos atributos no models
                              {'class': 'form-group form-control', #Aplicando formatação pronas do bootstrap
                               'placeholder': 'Informe o nome do aluno',
                               'autocomplete': 'off',
                               "title":"Aluno name"}),
            'email': forms.EmailInput(attrs=
                                    {'class': 'form-group form-control',  # Aplicando formatação pronas do bootstrap
                                     'placeholder': 'Informe o email do aluno',
                                     'autocomplete': 'off',
                                     "title": "Aluno email"}),
            'matricula': forms.TextInput(attrs=
                                     {'class': 'form-group form-control',  # Aplicando formatação pronas do bootstrap
                                      'placeholder': 'Informe a matricula do aluno',
                                      'autocomplete': 'off',
                                      "title": "Aluno matricula"}),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_curso'].widget.attrs = {'class': 'form-group form-control'}

class AtividadeForms(forms.ModelForm):
    class Meta:
        model = AtividadeExtracurricular  # classe de modelo (criada no models)
        fields = '__all__' #ou criar uma lista especificando quais campos vc quer usar
        labels = {'nome': 'Nome da Atividade'}  # configura o texto do label
        widgets = {
            'nome': forms.TextInput(
                attrs=  # A ordem dos campos pode seer facilmente mudada pela ordem dos atributos no models
                {'class': 'form-group form-control',  # Aplicando formatação pronas do bootstrap
                 'placeholder': 'Informe o nome da atividade extracurricular',
                 "title": "Atividade name"}),
            'descricao': forms.Textarea(attrs=
                                         {'class': 'form-group form-control',
                                          'placeholder': 'Descrição da atividade extracurricular',
                                          "title": "Descricao",
                                          'rows': 6}),
            'tipo': forms.Select(attrs=
                                      {'class': 'form-group form-select',  # Aplicando formatação pronas do bootstrap
                                       'placeholder': 'Informe o tipo da atividade extracurricular',
                                       "title": "Tipo da atividade"},
                                     choices=[('Pesquisa', 'Pesquisa'),
                                              ('Extenção', 'Extenção')]
                                     ),
            'situacao': forms.Select(attrs={'class': 'form-group form-select',  # Aplicando formatação pronas do bootstrap
                                       'placeholder': 'Informe a situação da atividade extracurricular',
                                       "title": "Situação da atividade"},
                                     choices=[('Ativo', 'Ativo'),
                                              ('Inativo', 'Inativo')]),
            'data_inicio': forms.DateInput(attrs=
                                          {'class': 'form-group form-control',
                                           'type': 'date',
                                           # Aplicando formatação pronas do bootstrap
                                           'placeholder': 'Informe a data de inicios da atividade',
                                           "title": "Data inicio"}
                                          ),
            'data_termino': forms.DateInput(attrs=
                                   {'class': 'form-group form-control',  # Aplicando formatação pronas do bootstrap
                                    'placeholder': 'Informe a data de termino da atividade',
                                    'type': 'date',
                                    "title": "Data termino"})


         }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['docente'].widget.attrs = {'class': 'form-group form-control'}

class ImagensForms(forms.ModelForm):
    class Meta:
        model = Imagens
        fields = '__all__'
        labels = {'nome': 'Nome da Atividade'}  # configura o texto do label
        widgets = {
            'descricao': forms.TextInput(
                attrs=  # A ordem dos campos pode seer facilmente mudada pela ordem dos atributos no models
                {'class': 'form-group form-control',  # Aplicando formatação pronas do bootstrap
                 'placeholder': 'Informe a descrição da imagem',
                 "title": "Imagem name"}),

            'arquivo': forms.FileInput(attrs=
                                     {'class': 'form-group form-control',  # Aplicando formatação pronas do bootstrap
                                      "title": "Arquivo da imagem"}),
            'extensao': forms.Select(attrs=
                                      {'class': 'form-group form-select',  # Aplicando formatação pronas do bootstrap
                                       'placeholder': 'Informe o tipo da atividade extracurricular',
                                       "title": "Tipo da atividade"},
                                      choices=[('.png', '.png'),
                                              ('.jpg', '.jpg'),
                                               ('.jpeg', '.jpeg'),])
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_atividade_extracurricular'].widget.attrs={'class': 'form-group form-control'}

class AlunoParticipaForms(forms.ModelForm):
    class Meta:
        model = AlunoParticipa  # classe de modelo (criada no models)
        fields = '__all__'
        # exclude = ["ativo"]  # campos que não serão exibidos
        labels = {'nome': 'Nome do registro'}  # configura o texto do label
        widgets = {
            'data_inicio': forms.DateInput(attrs= #A ordem dos campos pode seer facilmente mudada pela ordem dos atributos no models
                              {'class': 'form-group form-control', #Aplicando formatação pronas do bootstrap
                               'placeholder': 'Informe a data do inicio da participação',
                               'type': 'date',
                               "title":"Data de Inicio"}),
            'data_final': forms.DateInput(attrs=
                                    {'class': 'form-group form-control',  # Aplicando formatação pronas do bootstrap
                                     'placeholder': 'Informe do término da participação ',
                                     'type': 'date',
                                     "title": "Data de Término"}),
            'carga_horaria_semanal': forms.NumberInput(attrs=
                                     {'class': 'form-group form-control',  # Aplicando formatação pronas do bootstrap
                                      'placeholder': 'Informe a carga horária da participação',
                                      "title": "Carga Horária"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_atividade_extracurricualar'].widget.attrs = {'class': 'form-group form-control'}
        self.fields['fk_atividade_extracurricualar'].label = "Atividade Extracurricular"
        self.fields['fk_aluno'].widget.attrs = {'class': 'form-group form-control'}
        self.fields['fk_aluno'].label = "Aluno Participante"

class ColaboradoresForm(forms.ModelForm):
    class Meta:
        model = Colaboradores  # classe de modelo (criada no models)
        fields = '__all__'
        # exclude = ["ativo"]  # campos que não serão exibidos
        labels = {'nome': 'Nome do Colaborador'}  # configura o texto do label
        widgets = {
            'data_inicio': forms.DateInput(attrs= #A ordem dos campos pode seer facilmente mudada pela ordem dos atributos no models
                              {'class': 'form-group form-control', #Aplicando formatação pronas do bootstrap
                               'placeholder': 'Informe a data do inicio da participação',
                               'type': 'date',
                               "title":"Data de Inicio"}),
            'data_final': forms.DateInput(attrs=
                                    {'class': 'form-group form-control',  # Aplicando formatação pronas do bootstrap
                                     'placeholder': 'Informe do término da participação',
                                     'type': 'date',
                                     "title": "Data de Término"}),
            'situacao': forms.Select(attrs=
                                     {'class': 'form-group form-select',  # Aplicando formatação pronas do bootstrap
                                      'placeholder': 'Informe o tipo da atividade extracurricular',
                                      "title": "Tipo da atividade"},
                                     choices=[('Ativo', 'Ativo'),
                                              ('Inativo', 'Inativo')])
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_atividade_extracurricular'].widget.attrs = {'class': 'form-group form-control'}
        self.fields['fk_atividade_extracurricular'].label = "Atividade Extracurricular"
        self.fields['fk_docente'].widget.attrs = {'class': 'form-group form-control'}
        self.fields['fk_docente'].label = "Docente Colaborador"

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        # exclude = ["ativo"]  # campos que não serão exibidos
        labels = {'nome': 'Nome do Curso'}
        widgets = {
            'nome': forms.TextInput(
                attrs=
                {'class': 'form-group form-control',
                 'placeholder': 'Informe o nome do curso',
                 'autocomplete': 'off',
                 "title": "Nome do Curso"}),

            'codigo': forms.TextInput(attrs=
                                          {'class': 'form-group form-control',  # Aplicando formatação pronas do bootstrap
                                           'placeholder': 'Informe o código do curso',
                                           'autocomplete': 'off',
                                           "title": "Código do Curso"}),
            'descricao': forms.Textarea(attrs=
                                     {'class': 'form-group form-control',  # Aplicando formatação pronas do bootstrap
                                      'placeholder': 'Informe a Descrição do curso',
                                      'autocomplete': 'off',
                                      "title": "Decriçao do Curso"},)
        }