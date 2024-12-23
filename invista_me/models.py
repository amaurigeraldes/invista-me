from django.db import models
from datetime import datetime

# Documentação sobre models: https://docs.djangoproject.com/en/4.2/topics/db/models/

# Create your models here.

# Criando o Banco de Dados Investimento
class Investimento(models.Model):
    # Incluindo os campos do BD e definindo os tipos dos dados
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
    
# Após criar ou alterar campos do BD, executar as linhas abaixo no Terminal do VS Code:
# python manage.py makemigrations
# python manage.py migrate

# Verificando quais foram os comandos SQL utilizados pelo makemigrations executar a linha abaixo no Terminal do VS Code
# Obs.1: invista_me é o nome do projeto
# Obs.2: 0001_initial por exemplo, é o nome de um arquivo gerado pelo makemigrations dentro da pasta migrations
# python manage.py sqlmigrate invista_me 0001_initial


