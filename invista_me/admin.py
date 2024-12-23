from django.contrib import admin

# Importando as Tabelas do Banco de Dados para que apareçam no painel de gerenciamento do Django Admin
from .models import Investimento
admin.site.register(Investimento)

# Register your models here.
