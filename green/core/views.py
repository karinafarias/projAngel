from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from core.models import Polo, Terminal


# Create your views here.
def index(request):
    polos = Polo.objects.all()
    dados = {'listaPolos': polos}
    return render(request, 'index.html', dados)

def cadastrarPolo(request):
    return render(request, 'cadastrarPolo.html')

def cadastro(request):
    if request.method == 'POST':
        novoPolo = request.POST['novoPolo']
        if not novoPolo.strip():
            print ('Campo nome do polo está em branco.')
            return redirect('cadastro')
        if Polo.objects.filter(nomePolo=novoPolo).exists():
            print ('Polo já cadastrado')
            return redirect('cadastro')
        polo = Polo.objects.create(nomePolo=novoPolo, qtdEstoque=0)
        polo.save()
        print('Polo cadastrado com sucesso')
        return redirect('/')
    else:
        return render(request, 'cadastrarPolo.html')

def consultarPolo(request, idPolo):
    polo = get_object_or_404(Polo, pk=idPolo)
    dadoPolo = {
        'polo': polo
    }
    terminal = Terminal.objects.filter(idPoloT = polo)

    return render(request, 'consultarPolo.html', dadoPolo)





