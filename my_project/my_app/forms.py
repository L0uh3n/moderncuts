from django.forms import ModelForm
from django import forms
from my_app.models import usuario, comentario, agendamento

# Create the form class.
class ClientForm(ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Digite seu nome', 'required' : 'True'}))
    sobrenome = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Digite seu sobrenome', 'required' : 'True'}))
    data_nasc = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'required' : 'True'}))
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Digite seu nome de usuário', 'required' : 'True'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'Digite seu e-mail', 'required' : 'True'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Crie sua senha', 'required' : 'True'}))
    confirma_senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Crie sua senha', 'required' : 'True'}))
    num_telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite seu número de telefone', 'onkeypress': 'regex_telefone(event)', 'maxlength': '15', 'required' : 'True'}))
    class Meta:
        model = usuario
        widgets = {'email': forms.EmailInput(), 'user': forms.TextInput(), 'password': forms.PasswordInput(),}
        fields = ['nome', 'sobrenome', 'data_nasc', 'usuario', 'email', 'senha', 'confirma_senha', 'num_telefone']

class LoginForm(ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Digite seu nome de usuário', 'required' : 'True'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'password', 'placeholder' : 'Digite sua senha', 'required' : 'True'}))
    class Meta:
        model = usuario
        widgets = {'user': forms.TextInput(), 'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha']

class ComentForm(ModelForm):
    class Meta:
        model = comentario
        fields = ['comentario']

# class AgendForm(ModelForm):
#     data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     num_telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '(DDD) 9123-4567', 'onkeypress': 'regex_telefone(event)', 'maxlength': '15'}))
#     class Meta:
#         model = agendamento
#         fields = ['nome', 'sobrenome', 'num_telefone', 'data', 'hora', 'observacoes']