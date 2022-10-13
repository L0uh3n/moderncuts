from django.db import models

# Create your models here.

# class cidade(models.Model):
#     cidade = models.CharField(max_length=50)
#     class estado(models.TextChoices):
#         AC = 'AC', _('Acre')
#         AL = 'AL', _('Alagoas')
#         AP = 'AP', _('Amapá')
#         AM = 'AM', _('Amazonas')
#         BA = 'BA', _('Bahia')
#         CE = 'CE', _('Ceará')
#         ES = 'ES', _('Espírito Santo')
#         GO = 'GO', _('Goiás')
#         MA = 'MA', _('Maranhão')
#         MT = 'MT', _('Mato Grosso')
#         MS = 'MS', _('Mato Grosso do Sul')
#         MG = 'MG', _('Minas Gerais')
#         PA = 'PA', _('Pará')
#         PB = 'PB', _('Paraíba')
#         PR = 'PR', _('Paraná')
#         PE = 'PE', _('Pernambuco')
#         PI = 'PI', _('Piauí')
#         RJ = 'RJ', _('Rio de Janeiro')
#         RN = 'RJ', _('Rio Grande do Norte')
#         RS = 'RS', _('Rio Grande do Sul')
#         RO = 'RO', _('Rondônia')
#         RR = 'RR', _('Roraima')
#         SC = 'SC', _('Santa Catarina')
#         SP = 'SP', _('São Paulo')
#         SE = 'SE', _('Sergipe')
#         TO = 'TO', _('Tocantins')
#         DF = 'DF', _('Destrito Federal')

#     uf = models.CharField(
#         max_length=2,
#         choices=estado.choices,
#     )

# class endereco(models.Model):
#     logradouro = models.BigIntegerField(max_length=16)
#     numero_casa = models.CharField(max_length=16)
#     complemento = models.CharField(max_length=16)
#     cidade_id = models.CharField(max_length=16)
#     cep = models.IntegerField(max_length=16)
#     endereco_id = models.CharField(max_length=16)

class usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    usuario = models.CharField(max_length=30, unique=True)
    senha = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    num_telefone = models.CharField(max_length=20)

# class servicos(models.Model):
#     nome_servico = models.CharField(max_length=16)
#     valor_servico = models.CharField(max_length=16)

# class agendamento(models.Model):
#     servico_id = models.CharField(max_length=16)
#     cliente_id = models.CharField(max_length=16)
#     funcionario_id = models.CharField(max_length=16)
#     data_horario = models.CharField(max_length=16)
#     observacoes = models.CharField(max_length=16)

# class servicos_agendamento(models.Model):
#     servico_id = models.CharField(max_length=16)
#     agendamento_id = models.CharField(max_length=16)

# class categoria(models.Model):
#     tipo_categoria = models.CharField(max_length=16)

# class produtos(models.Model):
#     categoria_id = models.CharField(max_length=16)
#     descricao_produto = models.CharField(max_length=16)
#     estoque = models.CharField(max_length=16)
#     preco = models.CharField(max_length=16)

# class pedido(models.Model):
#     produto_id = models.IntegerField(max_length=16)
#     cliente_id = models.CharField(max_length=16)
#     data_pedido = models.CharField(max_length=16)
#     valor_produto = models.DecimalField(max_length=16)
#     qtde = models.CharField(max_length=16)
#     valor_total = models.CharField(max_length=16)

# class pagamento(models.Model):
#     cliente_id = models.IntegerField(max_length=16)
#     funcionario_id = models.CharField(max_length=16)
#     pedido_id = models.CharField(max_length=16)
#     valor = models.DecimalField(max_length=16)
#     qtde = models.CharField(max_length=16)
#     data_pagamento = models.CharField(max_length=16)