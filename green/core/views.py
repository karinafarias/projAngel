from django.shortcuts import render, get_object_or_404, get_list_or_404
from core.models import Polo, Terminal


# Create your views here.
def index(request):
    polos = Polo.objects.all()
    dados = {'listaPolos': polos}
    return render(request, 'index.html', dados)

def cadastrarPolo(request):
    return render(request, 'cadastrarPolo.html')

def consultarPolo(request, idPolo):
    polo = get_object_or_404(Polo, pk=idPolo)
    dadoPolo = {
        'polo': polo
    }
    terminal = Terminal.objects.filter(idPoloT = polo)

    return render(request, 'consultarPolo.html', dadoPolo)





