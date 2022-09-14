from django.shortcuts import render

# Create your views here.

def home (request):
    a = "Este é um teste em python"
    return render(request, 'home.html', {'variavel': a})

def games (request):
    return render(request, 'games.html', {})