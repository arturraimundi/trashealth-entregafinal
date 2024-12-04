from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PontodeColetaForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from .models import PontodeColeta
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout

def index(request):
        return render(request, 'index.html')

def mapa(request):
       return render(request, 'mapa.html')

def sac(request):
       return render(request, 'sac.html')

def nos(request):
       return render(request, 'nos.html')


  


def vitrine(request):
    context = {
        'vitrine': PontodeColeta.objects.all()  
    }
    return render(request, 'vitrine.html', context)

def pontomapa(request):
    pontos = PontodeColeta.objects.all()
    pontos_data = [
        {
            'titulo': ponto.titulo,
            'local': ponto.local,
            'coordenadaX': float(ponto.coordenadaX),
            'coordenadaY': float(ponto.coordenadaY)
        }
        for ponto in pontos
    ]
    context = {
        'pontos_json': json.dumps(pontos_data)
    }
    return render(request, 'mapa.html', context)



def erro(request):
     return render(request, 'erro.html')

def  erroCADASTRODEPONTO(request):
     return render(request, ' erroCADASTRODEPONTO.html')


from django.shortcuts import render
from django.contrib.auth.models import User
from validate_docbr import CNPJ  # Instale com pip install validate-docbr

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        # Validação de CNPJ
        cnpj_validator = CNPJ()
        if not cnpj_validator.validate(username):
            return render(request, 'register.html', {'error': 'CNPJ inválido'})

        # Verificar se o username ou email já existe
        user = User.objects.filter(username=username).first() or User.objects.filter(email=email).first()
        if user:
            return render(request, 'register.html', {'error': 'Usuário ou e-mail já cadastrado'})

        # Criar usuário
        user = User.objects.create_user(username=username, first_name=first_name, email=email, password=senha)
        user.save()

        return render(request, 'login.html')

     

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar o usuário
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)  # Registra o login na sessão
            return redirect('perfil')  # Redireciona para a view de perfil
        else:
            return messages.succes('Email ou senha inválidos')
         



@login_required
def CadastrodePontos(request):
    if request.method == 'POST':
        form = PontodeColetaForm(request.POST, request.FILES)
        if form.is_valid():
            # Obtendo o CNPJ do ponto e do usuário logado
            ponto_cnpj = form.cleaned_data.get('cnpj')
            user_cnpj = request.user.username

            # Verificando se os CNPJs coincidem
            if ponto_cnpj != user_cnpj:
                # Retorna uma página de erro (você pode personalizar o template de erro)
                return render(request,'erroCADASTRODEPONTO.html')

            # Salvando o ponto de coleta
            form.save()
            form = PontodeColetaForm()
            messages.success(request, 'Ponto de coleta cadastrado com sucesso.')
        else:
            return render(request,'erroCADASTRODEPONTO.html')
    else:
        form = PontodeColetaForm()
    
    context = {
        'form': form
    }
    return render(request, 'cadastropontos.html', context)

    


@login_required
def excluir_ponto(request, ponto_id):
    # Buscar o ponto pelo ID e verificar se pertence ao usuário logado
    ponto = get_object_or_404(PontodeColeta, id=ponto_id, cnpj=request.user.username)
    
    # Excluir o ponto
    ponto.delete()
    
    # Redirecionar de volta para o perfil
    return redirect('perfil')


@login_required
def perfil(request):
    username = request.user.username  # CNPJ do usuário logado
    first_name = request.user.first_name

    # Buscar pontos de coleta cadastrados com o mesmo CNPJ do usuário
    pontos = PontodeColeta.objects.filter(cnpj=username)

    return render(
        request,
        'perfil.html',
        {
            'username': username,
            'first_name': first_name,
            'pontos': pontos,  # Passando os objetos completos
        }
    )





def sair(request):
    logout(request)  # Remove o usuário da sessão
    return redirect('vitrine')  # Redireciona para a página inicial