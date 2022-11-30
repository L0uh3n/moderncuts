from django.forms import ModelForm
from django import forms
from my_app.models import usuario, comentario, agendamento, servicos

# Create the form class.
class ClientForm(ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Digite seu nome', 'required' : 'True'}))
    sobrenome = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Digite seu sobrenome', 'required' : 'True'}))
    data_nasc = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'required' : 'True'}))
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Digite seu nome de usuário', 'required' : 'True'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'Digite seu e-mail', 'required' : 'True'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Crie sua senha', 'maxlength': '30', 'required' : 'True'}))
    confirma_senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Confirme sua senha', 'maxlength': '30', 'required' : 'True'}))
    num_telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite seu número de telefone', 'onkeypress': 'regex_telefone(event)', 'maxlength': '15', 'required' : 'True'}))
    class Meta:
        model = usuario
        widgets = {'email': forms.EmailInput(), 'user': forms.TextInput(), 'password': forms.PasswordInput(),}
        fields = ['nome', 'sobrenome', 'data_nasc', 'usuario', 'email', 'senha', 'confirma_senha', 'num_telefone']

class LoginForm(ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Digite seu nome de usuário', 'required' : 'True'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Digite sua senha', 'maxlength': '30','required' : 'True'}))
    class Meta:
        model = usuario
        widgets = {'user': forms.TextInput(), 'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha']

class ComentForm(ModelForm):
    class Meta:
        model = comentario
        fields = ['comentario']

TIME_CHOICES = [
    ("08:00 às 09:00", "08:00 às 09:00"),
    ("09:00 às 10:00", "09:00 às 10:00"),
    ("10:00 às 11:00", "10:00 às 11:00"),
    ("11:00 às 12:00", "11:00 às 12:00"),
    ("13:00 às 14:00", "13:00 às 14:00"),
    ("14:00 às 15:00", "14:00 às 15:00"),
    ("15:00 às 16:00", "15:00 às 16:00"),
    ("16:00 às 17:00", "16:00 às 17:00"),
    ("17:00 às 18:00", "17:00 às 18:00"),
    ("18:00 às 19:00", "18:00 às 19:00"),
]

class AgendamentoForm(ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Digite seu nome', 'required' : 'True'}))
    sobrenome = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Digite seu sobrenome', 'required' : 'True'}))
    num_telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite seu número de telefone', 'onkeypress': 'regex_telefone(event)', 'maxlength': '15', 'required' : 'True'}))
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'required' : 'True'}))
    hora = forms.ChoiceField(choices = TIME_CHOICES,)
    class Meta:
        model = agendamento
        fields = [ 'nome', 'sobrenome', 'num_telefone', 'data', 'hora', 'observacoes']

class ServicosForm(ModelForm):
    servico = forms.CharField() 
    valor = forms.IntegerField()
    class Meta:
        model = servicos
        fields = ['servico', 'valor']