from django.shortcuts import render, redirect
from my_app.forms import ClientForm, LoginForm
from my_app.models import usuario
# Create your views here.

def home(request):
	profile = {}
	try:
		profile['perfil'] = usuario.objects.get(id=request.session['uid'])
		return render(request, 'home.html', profile)
	except:
		return render(request, 'home.html')

def login (request):
	data = {}
	data['login'] = LoginForm()
	return render(request, 'login.html', data)

def login_error (request):
	return render(request, 'login_error.html')

def logout (request):
	return render(request, 'logout.html')

def register (request):
	data = {}
	data['form'] = ClientForm()
	return render(request, 'register.html', data)

def register_sucess (request):
	return render(request, 'register_sucess.html')

def register_error (request):
	return render(request, 'register_error.html')

def docad(request):
	data = {}
	users = usuario.objects.all()
	form = ClientForm(request.POST or None)
	erro = ''
	for c in users:
		if form['usuario'].data == c.usuario:
			erro = 'User already exists'
			return render(request, 'register_error.html', data)
	if form.is_valid() and erro == '':
		form.save()
	return render(request, 'register_sucess.html', data)

def dolog(request):
	if request.method == 'POST':
		try:
			user = usuario.objects.get(usuario=request.POST['usuario']) # select * from usuario where usuario
		except:
			return redirect('login_error')
		print(user)
		if user.senha == request.POST['senha']:
			request.session['uid'] = user.id
			return redirect('home')
		else:
			return redirect('login_error')
	else:
		redirect('register')

	# users = usuario.objects.all()
	# form = ClientForm(request.POST or None)
	# for c in users:
	# 	if form['usuario'].data == c.usuario and form['senha'].data == c.senha:
	# 		return redirect('home')
	# for c in users:
	# 	if form['usuario'].data != c.usuario or form['senha'].data != c.senha:
	# 		return redirect('login_error')

def doout(request):
	if request.session['uid'] != "" or request.session['uid'] != None:
		try:
			del request.session['uid'] # finaliza a sessão
			return redirect('logout')
		except KeyError:
			return redirect('home')
	return redirect('home')