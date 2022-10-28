from django.db import models

# Create your models here.

class usuario(models.Model):  
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    usuario = models.CharField(max_length=30, unique=True)
    senha = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    num_telefone = models.CharField(max_length=15)

class comentario(models.Model):
    comentario = models.TextField (max_length=254)
    usuario = models.ForeignKey(usuario, on_delete = models.CASCADE)
    
class servicos(models.Model):
    servico = models.CharField(max_length=50)
    valor_servico = models.DecimalField(max_digits=5, decimal_places=2)

class agendamento(models.Model):
    servico = models.ForeignKey(servicos, on_delete = models.CASCADE)
    usuario = models.ForeignKey(usuario, on_delete = models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    observacoes = models.TextField(max_length=254, null=True)

class servicos_agendamento(models.Model):
    servico = models.ForeignKey(servicos, on_delete = models.CASCADE)
    agendamento = models.ForeignKey(agendamento, on_delete = models.CASCADE)