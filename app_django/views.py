from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conta
from django.db import IntegrityError
from decimal import Decimal
import random
import requests
from decouple import config

api_key = config('API_KEY')
def obter_cotacoes():
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/BRL'
    resposta = requests.get(url)
    dados = resposta.json()    
    cotacoes = {
        'dolar': Decimal(dados["conversion_rates"].get("USD")),
        'euro': Decimal(dados["conversion_rates"].get("EUR"))
    }
    print(cotacoes)
    return cotacoes

def index(request):
    return render(request, 'index.html')

def criar_conta(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        moeda = request.POST['moeda']
        saldo = Decimal(request.POST['saldo'])
        numero = f"{random.randint(0,99999):05}"
        try:
            Conta.objects.create(nome_titular=nome, numero_conta=numero, moeda=moeda, saldo=saldo)
            return redirect('index')
        except IntegrityError as e:
            error_message = "Já existe uma conta com este nome no banco."
            return render(request,'criar_conta.html', {'error_message':error_message})
    return render(request, 'criar_conta.html')

def exibir_conta(request):
    nome = request.GET.get('nome', None)
    conta = None
    if nome:
        conta = Conta.objects.filter(nome_titular__iexact = nome).first()
    return render(request, 'exibir_conta.html', {'conta': conta, 'nome': nome})

def exibir_tudo(request):
    contas = Conta.objects.all()
    return render (request, 'exibir_tudo.html', {'contas': contas})

def deposito(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        valor = Decimal(request.POST['valor'])
        conta = Conta.objects.filter(nome_titular=nome).first()
        cotacoes = obter_cotacoes()

        if conta:
            if conta.moeda == 'dolar':
                valor *= cotacoes['dolar']
            elif conta.moeda == 'euro':
                valor *= cotacoes['euro']

            conta.saldo += valor
            conta.save()
            return redirect('index')
        else:
            return HttpResponse("Conta não encontrada")
    return render(request, 'deposito.html')

def saque(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        valor = Decimal(request.POST['valor'])
        conta = Conta.objects.filter(nome_titular=nome).first()
        cotacoes = obter_cotacoes()

        if conta:
            if conta.moeda == 'dolar':
                valor *= cotacoes['dolar']
            elif conta.moeda == 'euro':
                valor *= cotacoes['euro']
            if conta.saldo >= valor:
                conta.saldo -= valor
                conta.save()
                return redirect('index')
            else:
                return HttpResponse("Saldo Insuficiente")
        else:
            return HttpResponse("Conta não encontrada")
    return render(request, 'saque.html')

def transferencia(request):
    if request.method == 'POST':
        nome_enviador = request.POST['nome_enviador']
        nome_recebedor = request.POST['nome_recebedor']
        valor = Decimal(request.POST['valor'])
        conta_enviador = Conta.objects.filter(nome_titular=nome_enviador).first()
        conta_recebedor = Conta.objects.filter(nome_titular=nome_recebedor).first()
        cotacoes = obter_cotacoes()

        if conta_enviador and conta_recebedor:

            if conta_enviador.moeda == 'dolar':
                valor_enviador = valor * cotacoes['dolar']
            elif conta_enviador.moeda == 'euro':
                valor_enviador = valor * cotacoes['euro']
            else:
                valor_enviador = valor

            if conta_recebedor.moeda =='dolar':
                valor_recebedor = valor * cotacoes['dolar']
            elif conta_recebedor.moeda == 'euro':
                valor_recebedor = valor * cotacoes['euro']
            else:
                valor_recebedor = valor
    
            if conta_enviador.saldo >= valor_enviador:
                conta_enviador.saldo -= valor_enviador
                conta_recebedor.saldo += valor_recebedor
                conta_enviador.save()
                conta_recebedor.save()
                return redirect('index')
            else:
                return HttpResponse("Saldo insuficiente")
        else:
            return HttpResponse("Conta(s) não encontrada")
    return render(request, 'transferencia.html')



