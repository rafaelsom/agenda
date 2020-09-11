from django.shortcuts import render, redirect
from core.models import Evento      #imortat core.models -> para listar toddos eventos cadastrados

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
#listar todos eventos cadastrados
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
