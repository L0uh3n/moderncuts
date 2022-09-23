from django.shortcuts import render, redirect
from my_app.forms import UsersForm
from my_app.models import Usuarios
# Create your views here.

def home(request):
	tabela = Usuarios.objects.all()
	return render(request, 'home.html', {'usuario': tabela})

def games (request):
    return render(request, 'games.html', {})

def register(request):
	data = {}
	data['form'] = UsersForm()
	return render(request, 'register.html', data)

def docad(request):
	users = Usuarios.objects.all()
	form = UsersForm(request.POST or None)
	erro = ''
	for c in users:
		if form['usuario'].data == c.usuario:
			erro = 'User already exists'
	if form.is_valid() and erro == '':
		form.save()
	return redirect('register')