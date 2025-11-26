Manual de Instalação e Utilização do Software

Este manual descreve o processo de instalação do sistema web BeyondClass, uma plataforma web desenvolvida em Python utilizando o framework Django, e o guia para sua utilização básica. O objetivo é fornecer as instruções necessárias para configurar o ambiente de desenvolvimento e executar a aplicação, além de detalhar as principais funcionalidades disponíveis para os usuários Docentes e Administradores.

A instalação da plataforma BeyondClass requer a configuração de um ambiente de desenvolvimento que suporte as tecnologias utilizadas no projeto.

Pré-requisitos de Instalação

Para executar a aplicação, os seguintes componentes de software devem estar instalados no sistema operacional:

1.  Python 3.7 ou superior: A linguagem de programação principal do código.
2.  Git: Para clonar o repositório do código-fonte ou pode baixar diretamente do GitHub e botar na pasta do projeto.
3.  PostgreSQL: O Sistema Gerenciador de Banco de Dados utilizado para persistência dos dados. É necessário que o servidor PostgreSQL esteja instalado e em execução.
4.  Editor de Código: Sugere-se o uso de uma IDE, como o PyCharm, conforme utilizado no desenvolvimento pois foi a que melhor se adequou.

Passos de Instalação

Passo 1: Clonar o Repositório (Caso queira clonar o repositório git diretamente)

Utilize o Git para baixar o código-fonte do projeto para sua máquina local, digitando o seguinte comendo no terminal.

git clone https://github.com/Mateus-Otavio/pfi_projeto1

Passo 2: Criar e Ativar o Ambiente Virtual

É altamente recomendado o uso de um ambiente virtual para isolar as dependências do projeto.

Cria o ambiente virtual
python -m venv venv

Ativa o ambiente virtual (Linux/macOS)
source venv/bin/activate

Ativa o ambiente virtual (Windows)
.\venv\Scripts\activate

Caso esteja usando o PyCharm com alguma licença jetbrains torna-se mais interessante criar um projeto django por meio dos recursos que essa licença disponibiliza pois ela já cria o ambiente virtual automaticamente, e ou outros comandos como o runserver são resumidos ao botão play.


Passo 3: Instalar as Dependências do Projeto

Com o ambiente virtual ativo, instale todas as bibliotecas Python necessárias por meio do terminal.
 pip install django pillow
 pip install django-widget-tweaks


Passo 4: Configurar o Banco de Dados

1.  Crie um banco de dados vazio no PostgreSQL (ex: `beyondclass_db`).
2.  Edite o arquivo "settings.py" do projeto Django para configurar a conexão com o banco de dados PostgreSQL, substituindo as credenciais padrão pelas suas:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'beyondclass_db',  # Nome do DB criado
        'USER': 'seu_usuario',      # Seu usuário do PostgreSQL
        'PASSWORD': 'sua_senha',    # Sua senha
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Passo 5: Executar as Migrações do Banco de Dados

Este comando ao ser utilizado no terminal aplicará as estruturas de tabelas (models) definidas no código para o banco de dados PostgreSQL.

python manage.py makemigrations
python manage.py migrate


Passo 6: Criar o Super Usuário

Crie um usuário com permissões de Administrador para acessar o painel de gerenciamento. Este será o primeiro usuário do sistema. Digite no terminal:

python manage.py createsuperuser

O sistema solicitará um nome de usuário, e-mail e senha.

Passo 7: Iniciar o Servidor de Desenvolvimento

Inicie a aplicação localmente com:

python manage.py runserver

Ou com o botão play caso esteja com um licença ativa como dito anteriormente.

Após a execução bem-sucedida, o sistema estará acessível no seu navegador pelo endereço que será gerado no terminal.

A plataforma BeyondClass foi desenvolvida para ser utilizada primariamente por Administradores e Docentes no gerenciamento das atividades extracurriculares.

-Acesso e Login

	Visualização Pública: Ao acessar a URL principal do sistema, a tela inicial é exibida, apresentando as atividades extracurriculares disponíveis na instituição. Esta tela é 	acessível a todos, sem a necessidade de login. 

	Login: Docentes e Administradores devem clicar no botão "Entrar" para fazerem o Login assim conseguindo acessar as funcionalidades de gerenciamento. A tela de 	Perfil com o ícone 	de um boneco, também permite ao usuário autenticado realizar o logout da sessão por meio do botão "Sair".

E necessário destacar que no primeiro acesso o login pode ser feito pelos mesmos dados usados para criar o super usuário (Nome de Usuário e senha), caso queira adicionar mais usuários necessita ir na url digitar /admin após a porta do django que é a 8000 normalmente e acessar a área do administrador com o Nome de Usuário e senha do super usuario para que possa adicionar um usuário e o vincular a um docente.

-Gerenciamento de Atividades Extracurriculares 

A funcionalidade central do sistema é o gerenciamento completo de atividades.

  Criação de Atividade: O Docente pode iniciar o processo de criação de uma nova atividade extracurricular por meio do botão "Cadastrar" na tela das atividades extracurriculares.

  Gestão de Detalhes: Após a criação, o Docente tem acesso à tela de gerenciamento da atividade, onde pode editar, excluir a atividade e consultar todas as suas informações.

  Adição de Imagens: É possível adicionar imagens à atividade por meio do botão “Adicionar imagens à Atividade”, que serão exibidas em um carrossel na página pública. O objetivo é aumentar      o engajamento e a transparência da atividade.

-Gestão de Participantes

O Docente é o responsável por controlar a participação de alunos e colaboradores em suas atividades.

  Adicionar Alunos: Através do botão “Ver alunos participantes” na tela de gerenciamento, o Docente pode visualizar os estudantes já inscritos e adicionar novos alunos à atividade,   registrando uma participação por meio do botão "Cadastrar".
  Cadastrar Colaboradores: O sistema permite o cadastro de colaboradores para a atividade, essencial para o auxílio na execução e administração do projeto.

