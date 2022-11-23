from django.forms import ModelForm
from django import forms
from my_app.models import usuario, comentario, agendamento

# Create the form class.
class ClientForm(ModelForm):
    data_nasc = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    senha = forms.CharField(widget=forms.PasswordInput)
    num_telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '(DDD) 9123-4567', 'onkeypress': 'regex_telefone(event)', 'maxlength': '15'}))
    class Meta:
        model = usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['nome', 'sobrenome', 'data_nasc', 'usuario', 'email', 'senha', 'num_telefone']

class LoginForm(ModelForm):
    usuario = forms.CharField(widget=forms.CharField(attrs={'placeholder' : 'Digite seu nome de usuário', 'required' : 'True'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Digite sua senha', 'required' : 'True'}))
    class Meta:
        model = usuario
        widgets = {'password': forms.PasswordInput(),}
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