from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email
# Create your views here.
def login(request):
    return render(request, 'conta/login.html')


def logout(request):
    return render(request, 'conta/logout.html')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'conta/cadastro.html')
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    if not nome or not email or not senha:
        messages.error(request, 'Ta errado cara')
        return render(request, 'conta/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'email invalido')
        return render(request, 'conta/cadastro.html')
    return render(request, 'conta/cadastro.html')


def dashboard(request):
    return render(request, 'conta/dashboard.html')