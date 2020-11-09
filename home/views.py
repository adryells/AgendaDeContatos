from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contato
from django.contrib import messages
# Create your views here.
def index(request):
    messages.add_message(request, messages.ERROR, 'Erro Ocorrido!')
    contatos = Contato.objects.order_by('-id')
    paginator = Paginator(contatos, 5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'home/home.html',{
        'contatos': contatos
    })
#comentario

def ver_contato(request,contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request,'home/ver_contato.html',{
        'contato': contato
    })

def busca(request):
    termo = request.GET.get('termo')
    contatos = Contato.objects.order_by('-id').filter(
        nome__icontains = termo,
        mostrar = True
    )
    page = request.GET.get('p')
    paginator = Paginator(contatos, 5)
    return render(request, 'home/busca.html', {
        'contatos': contatos
    })