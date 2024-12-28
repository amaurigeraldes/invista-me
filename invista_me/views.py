# Importando a biblioteca HttpResponse para utilização na função pagina_inicial()
from django.shortcuts import render, HttpResponse, redirect

# Importando as informações que estão registradas no Banco de Dados para passá-las para a Página
from .models import Investimento

# Importando o formulário que foi criado
from .forms import InvestimentoForm

# Importando a biblioteca da funcionalidade que permite acesso a determinadas rotas somente fazendo Login
# Obs.: usar o decorator @login_required nas páginas que desejar
from django.contrib.auth.decorators import login_required


# Create your views here.

""" 
# Criando a página inicial
def pagina_inicial(request):
    # Retornando um processo Http
    return HttpResponse('Pronto para investir!')
 """

# Criando a página contato
def contato(request):
    # Retornando um processo Http
    return HttpResponse('No caso de dúvidas, enviar um e-mail para contato@suporte.com.br')

""" 
# Criando a página minha história
def minha_historia(request):
    # Retornando uma página 
    # Criando um dicionário e atribuindo à variável pessoa
    # Obs.: poderia retornar informações de um Banco de Dados
    pessoa = {
        'nome': 'Jeff',
        'idade': 28,
        'hobby': 'Games'
    }
    # Usando a função render e passando o caminho para a pasta templates
    # return render(request, 'investimentos/minha_historia.html) # passando dados estáticos
    # Incluindo o parâmetro pessoa para passar dados dinâmicos vindos do servidor
    return render(request, 'investimentos/minha_historia.html', pessoa)

# Criando a página novo investimento
def novo_investimento(request):
    # Usando a função render e passando o caminho para a pasta templates
    return render(request, 'investimentos/novo_investimento.html')

# Criando a página investimento registrado
def investimento_registrado(request):
    # Criando um dicionário e atribuindo à variável investimento
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    # Usando a função render e passando o caminho para a pasta templates
    return render(request, 'investimentos/investimento_registrado.html', investimento)
"""

# Criando a página investimentos
def investimentos(request):
    # Criando um dicionário para passar as informações do BD para a Página
    # Obs.: trazendo todos os registros do BD para o dicionário
    dados = {
        'dados': Investimento.objects.all()
    }
    # Usando a função render e passando o caminho para a pasta templates
    return render(request, 'investimentos/investimentos.html', context=dados)

# Criando a página detalhe
def detalhe(request, id_investimento):
    
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    # Usando a função render e passando o caminho para a pasta templates
    return render(request, 'investimentos/detalhe.html', dados)

# Criando a página criar (CRUD Create)
@login_required
def criar(request):
    # Verificando qual foi o tipo de requisição foi efetuada 
    # Obs.: se está sendo criado algo novo ou atualizando alguma informação já existente
    if request.method == 'POST':
        # Acessando as informações que foram preenchidas na Tela e atribuindo à variável
        investimento_form = InvestimentoForm(request.POST)
        # Validar se as informações foram corretamente preenchidas
        if investimento_form.is_valid():
            # Salvando as informações
            investimento_form.save()
        # Redirecionando para a página inicial 
        return redirect('investimentos')
    # Caso não seja um POST, criar um formulário do zero
    else:
        # Instanciando a classe
        investimento_form = InvestimentoForm()
        # Criando um Dicionário que será passado para a Página
        formulario = {
            'formulario': InvestimentoForm
        }
        # Usando a função render e passando o caminho para a pasta templates
        return render(request, 'investimentos/novo_investimento.html', context=formulario)


# Criando a página editar (CRUD Update)
# Obs.: recebe a requisição que está sendo passada e o id_investimento
@login_required
def editar(request, id_investimento):
    # Obtendo a informação do Banco de Dados atráves da primary key id_investimento e atribuindo a uma variável
    investimento = Investimento.objects.get(pk=id_investimento)
    # Verificando qual foi o tipo de requisição foi efetuada 
    # Obs.: se está sendo criado algo novo ou atualizando alguma informação já existente
    # Caso a requisição seja um GET
    if request.method == 'GET':
        # Populando o formulário com informações do BD e atribuindo a uma variável
        formulario = InvestimentoForm(instance=investimento)
        # Retornando o formulário já preenchido para a mesma página utilizada para criar novos investimentos
        # Obs.: para passar os dados, criar e passar como parâmetro um Dicionário com a Chave formulario e o formulario em sí
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    # Quando já estamos em uma página e pressionamos o Botão Submit enviando os dados da página, não estamos mais fazendo um GET (buscando dados) mas sim um POST (enviando dados), que estamos atualizando
    # Caso contrário, a requisição seja um POST
    if request.method == 'POST':
        # Acessando as informações que foram preenchidas na Tela e atribuindo à variável
        # Obs.: passando o parâmetro instance=investimento para a atualização das informações no BD 
        formulario = InvestimentoForm(request.POST, instance=investimento)
        # Validar se as informações foram corretamente preenchidas
        if formulario.is_valid():
            # Salvando as informações
            formulario.save()
        # Redirecionando para a página inicial 
        return redirect('investimentos')
    

# Criando a página excluir (CRUD Delete)
# Obs.: recebe a requisição que está sendo passada e o id_investimento
@login_required
def excluir(request, id_investimento):
    # Obtendo a informação do Banco de Dados atráves da primary key id_investimento e atribuindo a uma variável
    investimento = Investimento.objects.get(pk=id_investimento)
    # Verificando qual foi o tipo de requisição foi efetuada 
    # Obs.: se está sendo criado algo novo ou atualizando alguma informação já existente
    # Caso seja um POST (enviando dados)
    if request.method == 'POST':
        # Excluindo a informação do BD
        investimento.delete()
        # Redirecionando para a página inicial 
        return redirect('investimentos')
    # Caso seja um GET (buscando dados) redirecionar para a 
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})
        