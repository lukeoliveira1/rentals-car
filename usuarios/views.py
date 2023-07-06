from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import NewUserForm, clienteForm
from .models import Client
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.

#user

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("carros_urls:paginaInicial")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	
	form = NewUserForm()	
	return render (request=request, template_name="cadastros/cadastrarUsuario.html", context={"register_form":form})


def my_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user) 
				return redirect("carros_urls:paginaInicial") 
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login/login.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Você realizou logout com sucesso!") 
	return redirect("carros_urls:paginaInicial")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("carros_urls:paginaInicial")
		messages.error(request, "Unsuccessful registration. Invalid information.")	
	form = NewUserForm()
	return render (request=request, template_name="cadastros/cadastrarUsuario.html", context={"register_form":form})


#cliente

def cadastrarCliente(request):

    if request.method == 'GET':
        form = clienteForm()
        context = {'formCliente' : form}
        print('--Entrou')
        return render(request, "clientes/formClientes.html", context)
    
    else:
        form = clienteForm(request.POST) 

        if  form.is_valid(): 
            form.save()
            form = clienteForm()

        context = {'formCliente' : form}
        return render(request, "clientes/formClientes.html", context)

def listarClientes(request):
    clientes = Client.objects.all()
    return render(request, "clientes/listarClientes.html", context={'clientes': clientes})

def deletarCliente(request, id):
 
    obj = get_object_or_404(Client, id = id)
 
    if request.method =="POST":

        obj.delete()

        return HttpResponseRedirect("/")
 
    return render(request, "clientes/formDelete.html")
    