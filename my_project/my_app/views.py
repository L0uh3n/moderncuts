from django.shortcuts import render, redirect
from my_app.forms import ClientForm, LoginForm, ComentForm
from my_app.models import usuario, comentario
# Create your views here.

def home (request):
	profile = {}
	try:
		profile['perfil'] = usuario.objects.get(id=request.session['uid'])
		profile['custom'] = 'Sair'
		return render(request, 'home.html', profile)
	except:
		profile['custom'] = 'Entrar'
		return render(request, 'home.html', profile)

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

def docad (request):
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

def dolog (request):
	if request.method == 'POST':
		try:
			user = usuario.objects.get(usuario=request.POST['usuario']) # select * from usuario where usuario.id = usuario da sessão
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

def doout (request):
	if request.session['uid'] != "" or request.session['uid'] != None:
		try:
			del request.session['uid'] # finaliza a sessão
			return redirect('logout')
		except KeyError:
			pass
	return redirect('home')

def profile (request):
	profile = {}
	try:
		profile['perfil'] = ClientForm(instance=usuario.objects.get(id=request.session['uid']))
		return render (request, 'profile.html', profile)
	except:
		return redirect('login')
 
def doupdate (request):
	form = usuario.objects.get(id=request.session['uid'])
	form.nome = request.POST['nome']
	form.sobrenome = request.POST['sobrenome']
	form.usuario = request.POST['usuario']
	form.senha = request.POST['senha']
	form.email = request.POST['email']
	form.num_telefone = request.POST['num_telefone']
	form.save()
	return redirect('home')

def coment (request):
	data = {}
	if request.method == 'POST':
		c = comentario(usuario=usuario.objects.get(id=request.session['uid']), comentario=request.POST['comentario'])
		c.save()
		return redirect('home')
	else:
		data['form'] = ComentForm()
	return render(request, 'coment.html', data)

def agendamento (request):
	return render(request, 'agendamento.html')