from django.shortcuts import render, redirect
from my_app.forms import ClientForm, LoginForm, ComentForm, AgendamentoForm, ServicosForm
from my_app.models import usuario, comentario, agendamento, servicos, servicos_agendamento
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
	data['register'] = ClientForm()
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
		redirect('login')

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
		return redirect('home')
 
def doupdate (request):
	form = usuario.objects.get(id=request.session['uid'])
	form.nome = request.POST['nome']
	form.sobrenome = request.POST['sobrenome']
	form.usuario = request.POST['usuario']
	form.senha = request.POST['senha']
	form.email = request.POST['email']
	form.num_telefone = request.POST['num_telefone']
	form.save()
	return redirect('update_sucess')

def update_sucess (request):
	return render(request, 'update_sucess.html')

def coment (request):
	data = {}
	if request.method == 'POST':
		c = comentario(usuario=usuario.objects.get(id=request.session['uid']), comentario=request.POST['comentario'])
		c.save()
		return redirect('coment')
	else:
		data['form'] = ComentForm()
		data['history'] = comentario.objects.filter(usuario = request.session['uid'])
		return render(request, 'coment.html', data)

def edit_coment (request, id):
	c = comentario.objects.get(id=id)
	if request.method == 'POST':
		f = ComentForm(request.POST, instance=c)
		f.save()
		return redirect('coment')
	else:
		f = ComentForm(instance=c)
		return render(request, 'coment.html', {'form':f})

def agend(request):
	data = {}
	data['servico'] = servicos.objects.all()
	try:
		if request.method == 'POST':
			c = agendamento(usuario=usuario.objects.get(id=request.session['uid']), nome = request.POST['nome'], sobrenome = request.POST['sobrenome'], num_telefone = request.POST['num_telefone'], data = request.POST['data'], hora = request.POST['hora'], observacoes = request.POST['observacoes'])
			c.save()
			for i in request.POST:
				if i.find("-") != -1:
					print(i)
					sid = i.split("-")
					s = servicos_agendamento.objects.create(servico=servicos.objects.get(id=sid[1]), agendamento=c)
					s.save()
			return redirect('agend')
		else:
			data['agend'] = AgendamentoForm()
			data['history'] = agendamento.objects.filter(usuario=request.session['uid'])
			data['servico'] = servicos.objects.all()
			return render(request, 'agend.html', data)
	except KeyError:
		pass
	return redirect('login')

def agend_sucess (request):
	return render(request, 'agend_sucess.html')

def edit_agend(request, id):

	c = agendamento.objects.get(id=id)
	s = servicos.objects.get(id=id)
	sa = servicos_agendamento.objects.filter(servico_id=s)
	lista_servicos = {}
	
	# lista_servicos['servicos'] = sa

	if request.method == 'POST':
		# e = ServicosForm(request.POST, isinstance=sa)
		f = AgendamentoForm(request.POST, instance=c)
		# e.save()
		f.save()
		return redirect('agend')
	else:
		lista_servicos['servico'] = sa
		# e = ServicosForm(instance=sa)
		f = AgendamentoForm(instance=c)
		return render(request, 'agend.html', {'agend':f}, lista_servicos)

def agend_delete(request, id):
	c = agendamento.objects.get(id=id)
	c.delete()
	return redirect('agend')