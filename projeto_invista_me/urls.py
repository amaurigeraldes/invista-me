"""
URL configuration for projeto_invista_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# Importando o App que criamos da pasta invista_me (arquivo views.py)
from invista_me import views

# Importando o App que criamos da pasta usuarios (arquivo usuario_views.py)
# Obs.: para diferenciar do App anterior estamos usando o apelido usuario_views
from usuarios import views as usuario_views

# Importando a biblioteca da funcionalidade disponibilizado pelo Django para fazer Login e Logout
# Obs.: utilizando o apelido auth_views para diferenciar da outra views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Habilita o painel de gerenciamento do Django Admin
    path('admin/', admin.site.urls),
    
    # Criando uma rota para a página novo usuario para a criação de novos usuários
    # Obs.1: usando 'conta/' para acessar a rota estando dentro da página inicial
    # Obs.2: passando o parâmetro name='novo_usuario' para ser utilizado como referência na função novo_usuario em usuario_views.py
    path('conta/', usuario_views.novo_usuario, name='novo_usuario'),
    
    # Criando uma rota para a página login para fazer o login do usuário
    # Obs.1: importando o template .as_view() baseado na classe LoginView
    # Obs.2: passando o parâmetro template_name='usuarios/login.html' para especificar onde deverá ser buscado esse template, sendo que caso não seja específicado, por padrão será buscado em registration/login.html
    # Obs.3: usando esse Tipo de View (ClassBasedView) que lida com a lógica de autenticação/validação
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    
    # Criando uma rota para a página logout para fazer o logout do usuário
    # Obs.1: importando o template .as_view() baseado na classe LogoutView
    # Obs.2: passando o parâmetro template_name='usuarios/logout.html' para especificar onde deverá ser buscado esse template, sendo que caso não seja específicado, por padrão será buscado em registration/logout.html
    # Obs.3: usando esse Tipo de View (ClassBasedView) que lida com a lógica de autenticação/validação
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
        
    # Para definir um usuário e senha para o painel de gerenciamento do Django Admin executar no Terminal do VS Code
    # python manage.py createsuperuser
    
    # Para visualizar o projeto no Navegador executar no Terminal do VS Code
    # python manage.py runserver
    
    # Criando uma rota para a página inicial
    # path('', views.pagina_inicial),
    # Alterando a rota para que a página inicial se torne a página investimentos
    # Obs.: passando o parâmetro name='investimentos' para ser utilizado como referência na função investimentos em views.py
    path('', views.investimentos, name='investimentos'),
    
    # Criando uma rota para a página contato
    # path('contato/', views.contato, name='contato'),
    
    # Criando uma rota para a página minha_historia
    # path('minha_historia/', views.minha_historia, name='minha_historia'),
    
    # Criando uma rota para a página novo_investimento para criar um investimento
    # path('novo_investimento/', views.novo_investimento, name='novo_investimento'),
    # Alterando a rota para apontar para a função criar (CRUD Create) no arquivo views.py
    path('novo_investimento/', views.criar, name='novo'),
    
    # Criando uma rota para a página novo_investimento para editar um investimento
    # Obs.1: apontando para a função editar (CRUD Update) no arquivo views.py
    # Obs.2: usando <int:id_investimento> para receber um parâmetro dentro da URL
    path('novo_investimento/<int:id_investimento>', views.editar, name='editar'),
    
    # Criando uma rota para a página excluir_investimento para excluir um investimento
    # Obs.1: apontando para a função excluir (CRUD Delete) no arquivo views.py
    # Obs.2: usando <int:id_investimento> para receber um parâmetro dentro da URL
    path('excluir_investimento/<int:id_investimento>', views.excluir, name='excluir'),
    
    # Criando uma rota para a página investimento_registrado
    # path('investimento_registrado/', views.investimento_registrado, name='investimento_registrado'),
    
    # Criando uma rota para a página detalhe a partir da página investimentos (Página Inicial)
    # Obs.1: usando / por já estar dentro da página investimentos (Página Inicial)
    # Obs.2: usando <int:id_investimento> para receber um parâmetro dentro da URL
    path('/<int:id_investimento>', views.detalhe, name='detalhe'),
    
]
