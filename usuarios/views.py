from django.shortcuts import render, redirect

# Importando a biblioteca UserCreation Form 
# Obs.: foi desabilitada pois ativamos a UserRegisterForm
# from django.contrib.auth.forms import UserCreationForm

# Importando a biblioteca UserRegisterForm
# Obs.: foi criada a partir da UserCreationForm alterando o Padrão para inclusão de Novos Campos
from .forms import UserRegisterForm

# Importando a biblioteca que permite a geração de mensagens na tela do usuário
'''
messages.debug()
messages.info()
messages.success()
messages.warning()
messages.error()
'''
from django.contrib import messages

# Create your views here.

# Criando a página para a criação de Novos Usuários
# Obs.: a informação vem do Site(Navegador) para o Servidor(BackEnd) no formato de POST
def novo_usuario(request):
    # Verificando qual é o Tipo da Requisição
    if request.method == 'POST':
        # Utilizando a funcionalidade UserCreation Form que já existe pronto no Django
        # Instanciando e criando um Novo Formulário
        # Obs.: usando o parâmetro request.POST p/ pegar as informações enviadas do site p/ o servidor e populando a classe
        formulario = UserRegisterForm(request.POST)  # Substituição da UserRegisterForm
        # Validando se a informação foi preenchida corretamente
        if formulario.is_valid():
            # Salvando a informação no Banco de Dados
            formulario.save()
            # Extraindo da propriedade username, o nome do usuário que foi criado e atribuindo a uma variável
            usuario = formulario.cleaned_data.get('username')
            # Enviando uma mensagem na tela do usuário informando que o usuário foi criado
            messages.success(request, f'O usuário {usuario} foi criado com sucesso!')
            # Redirecionado o usuário para a página de Login
            return redirect('login')
    # Caso contrário
    else:
        # Criando uma formulário vazio e atribuindo a uma variável
        formulario = UserRegisterForm()  # Substituição da UserRegisterForm
    # Usando a função render e passando o caminho para a pasta templates, subpasta usuarios onde deverá ser criado o arquivo registrar.html
    # Obs.: as pastas e o arquivo html deverão ser criados dentro do App usuarios
    return render(request, 'usuarios/registrar.html', {'formulario': formulario} )