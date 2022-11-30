from django.db import models

# Create your models here.

class usuario(models.Model):  
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    usuario = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    senha = models.CharField(max_length=30)
    num_telefone = models.CharField(max_length=15)

class comentario(models.Model):
    comentario = models.TextField (max_length=254)
    usuario = models.ForeignKey(usuario, on_delete = models.CASCADE)

class agendamento(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    num_telefone = models.CharField(max_length=15)
    data = models.DateField()
    hora = models.CharField(max_length=120)
    observacoes = models.TextField(max_length=255, blank=True)

class servicos(models.Model):
    servico = models.CharField(max_length=120) 
    valor = models.IntegerField()
    preenchido = models.ManyToManyField(agendamento, through='servicos_agendamento')

class servicos_agendamento(models.Model):
    servico = models.ForeignKey(servicos, on_delete=models.CASCADE)
    agendamento = models.ForeignKey(agendamento, on_delete=models.CASCADE)