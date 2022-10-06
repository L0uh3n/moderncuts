from django.shortcuts import render, redirect
from my_app.forms import ClientForm
from my_app.models import usuario
# Create your views here.

def home(request):
	tabela = usuario.objects.all()
	return render(request, 'home.html', {'usuario': tabela})

def login (request):
	data = {}
	data['form'] = ClientForm()
	return render(request, 'login.html', data)

def register (request):
	data = {}
	data['form'] = ClientForm()
	return render(request, 'register.html', data)

def docad(request):
	users = usuario.objects.all()
	form = ClientForm(request.POST or None)
	erro = ''
	for c in users:
		if form['usuario'].data == c.usuario:
			erro = 'User already exists'
	if form.is_valid() and erro == '':
		form.save()
	return redirect('login')

def dolog(request):
	users = usuario.objects.all()
	form = ClientForm(request.POST or None)
	erro = ''
	for c in users:
		if form['usuario'].data != c.usuario and form['senha'].data != c.senha:
			erro = 'Username or password are incorrect'
	if form.is_valid() and erro == '':
		form.save()
	return redirect('home')