from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from alugueis.models import aluguel
from .forms import aluguelForm

# Create your views here.
def cadastrarLocacao(request):

    if request.method == 'GET':
        form = aluguelForm()
        context = {'primeiroForm' : form}
        print('--Entrou')
        return render(request, "aluguel/formAlugar.html", context)
    
    else:
        form = aluguelForm(request.POST) 

        if  form.is_valid(): 
            form.save()
            form = aluguelForm()

        context = {'primeiroForm' : form}
        return render(request, "aluguel/formAlugar.html", context)

def listarLocacoes(request):
    locacoes = aluguel.objects.all()
    return render(request, "aluguel/listarLocacoes.html", context={'locacoes': locacoes})

def deletarLocacao(request, id):
  
    obj = get_object_or_404(aluguel, id = id)
 
 
    if request.method =="POST":

        obj.delete()

        return HttpResponseRedirect("/")
 
    return render(request, "aluguel/formDelete.html")
    