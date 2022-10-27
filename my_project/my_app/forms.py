from django.forms import ModelForm
from django import forms
from my_app.models import usuario, comentario

# Create the form class.
class ClientForm(ModelForm):
    data_nasc = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    senha = forms.CharField(widget=forms.PasswordInput)
    num_telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '(DDD) 9123-4567', 'onkeypress': 'regex_telefone(event)', 'maxlength': '15'}))
    class Meta:
        model = usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['nome', 'sobrenome', 'data_nasc', 'usuario', 'senha', 'email', 'num_telefone']

class LoginForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha']

class ComentForm(ModelForm):
    class Meta:
        model = comentario
        fields = ['comentario']