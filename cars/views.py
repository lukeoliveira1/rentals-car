from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from cars.models import Car
from .forms import carroForm

# Create your views here.
def paginaInicial(request):
    produtos = Car.objects.all()
    return render(request, "paginaInicial.html", context={'produtos': produtos})

def detalheCarro(request, id_produto):
    print("O carro que você selecionou:", id_produto)
    produtos = Car.objects.get(id=id_produto)
    return render(request, "carros\detalheCarro.html", context={'produto': produtos})


def cadastrarCarro(request):
    if request.method == 'POST':
        form = carroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            produtos = Car.objects.all()
            context={'produtos': produtos}
            return render(request, "paginaInicial.html", context)

    else:
        form = carroForm
        context = {'formCarros': form}
        return render(request, "carros/formCarros.html", context)

def deletarCarro(request, id):
  
    obj = get_object_or_404(Car, id = id)
 
    if request.method =="POST":

        obj.delete()

        return HttpResponseRedirect("/")
 
    return render(request, "carros/formDelete.html")
    
