# Criar o arquivo froms.py dentro da Pasta do Projeto (no caso é a pasta invista_me)
# Importando a biblioteca ModelForm para a criação de um formulário
from django .forms import ModelForm

# Importando todos os modelos, todas as classes que representam tabelas no Banco de Dados
from .models import Investimento

# Criando um formulário usando uma Model Form e herdando de ModelForm
class InvestimentoForm(ModelForm):
    class Meta:
        # Definindo como queremos que este formulário seja criado
        model = Investimento
        # Lista de quais campos serão exibidos. Ex: ['valor', 'pago'] ou usar '__all__' para exibir todos os campos 
        fields = '__all__'
        