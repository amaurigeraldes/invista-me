# Importando as bibliotecas
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Modificando o Template cadastro de usuários padrão 
# Obs.: lógica que permite a inclusão de novos campos no formulário padrão

# Criando uma Nova Classe que será uma Nova Forma de Criar Usuários 
# Obs.: herdando da UserCreationForm para que não seja necessário recriar toda a funcionalidade que já existe
class UserRegisterForm(UserCreationForm):
    # Definindo os novos campos que desejamos adicionar
    # Obs.: vide documentação para saber mais sobre os Tipos de campos a serem criados
    # ​Link para documentação do UserCreationForm https://docs.djangoproject.com/en/3.2/ref/forms/fields/
    email = forms.EmailField()
    
    
    class Meta:
        # Definindo com qual modelo o usuário estará interagindo
        model = User
        # Definindo quais campos deverão ser criados sempre que chamar a classe UserRegisterForm
        fields = ['username', 'email', 'password1', 'password2']



