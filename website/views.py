from django.shortcuts import render
from website.models import Pessoa
from website.models import Ong

# Create your views here.

def index(request):


    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.data_nascimento = request.POST.get('data_nascimento')
        pessoa.email = request.POST.get('email')
        pessoa.str_cep = request.POST.get('str_cep')
        pessoa.str_numero = request.POST.get('str_numero')
        pessoa.complemento = request.POST.get('complemento')
        pessoa.genero = request.POST.get('genero')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.celular = request.POST.get('celular')
        pessoa.motivo = request.POST.get('motivo')
        pessoa.save()

        contexto = {
            'nome': pessoa.nome
        }
        return render(request, 'index.html', contexto)


    
    return render(request, 'index.html')

def pessoas(request):
    pessoas = Pessoa.objects.filter(ativo=True).all()
    
    contexto = {
        'pessoas': pessoas
    }
    return render(request, 'pessoas.html', contexto)


def ong(request):


    if request.method == 'POST':
        ong = Ong()
        ong.nome = request.POST.get('nome')
        ong.responsavel= request.POST.get('responsavel')
        ong.horario_funcionamento = request.POST.get('horario_funcionamento')
        ong.endereco= request.POST.get('endereco')
        ong.telefone = request.POST.get('telefone')
        ong.str_numero = request.POST.get('str_numero')
        ong.complemento = request.POST.get('complemento')
        ong.obs = request.POST.get('obs')
        ong.save()

        contexto = {    
            'nome': ong.nome
        }
        return render(request, 'ong.html', contexto)


    
    return render(request, 'ong.html')

def ongs(request):
    ongs = Ong.objects.filter(ativo=True).all()
    
    contexto = {    
        'ongs': ongs
    }
    return render(request, 'asongs.html', contexto)
