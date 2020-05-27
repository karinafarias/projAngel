from django.shortcuts import render, redirect
from core.models import Polo, Terminal


# Create your views here.
def index(request):
    return redirect('/listaPolo/')

def listaPolos (request):
    polos = Polo.objects.all()
    dados = {'listaPolo': polos}
    return render(request, 'index.html',dados)


def listaTerminais(request,id):
    idPoloT = request.GET.get(id)
    terminais = Terminal.objects.get(idPoloT=id)
    dados = {'listaTerminal': terminais}
    return render(request,'consultarPolo.html',dados)