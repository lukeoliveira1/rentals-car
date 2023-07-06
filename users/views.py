from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import NewUserForm, clientForm
from .models import Client
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

from django.views.generic import ListView, FormView, UpdateView, DetailView, DeleteView

# Create your views here.

#user

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("cars_urls:paginaInicial")
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
				return redirect("cars_urls:paginaInicial") 
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login/login.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Você realizou logout com sucesso!") 
	return redirect("cars_urls:paginaInicial")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("cars_urls:paginaInicial")
		messages.error(request, "Unsuccessful registration. Invalid information.")	
	form = NewUserForm()
	return render (request=request, template_name="cadastros/cadastrarUsuario.html", context={"register_form":form})


#cliente

class ClientListView(ListView):
    model = Client
    queryset = Client.objects.all()
    template_name = "clients/client_list.html"
    
class ClientCreateView(FormView):
    template_name = 'clients/client_form.html'
    form_class = clientForm
    success_url = reverse_lazy('users_urls:index')

    def form_valid(self, form):
        form.save()  # Salva o objeto Car no banco de dados
        return super().form_valid(form)

class ClientUpdateView(UpdateView):
    model = Client
    form_class = clientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('users_urls:list')

class ClientDetailView(DetailView):
    model = Client
    queryset = Client.objects.all()

class ClientDeleteView(DeleteView):
    model = Client
    slug_field = 'slug'  # campo de slug no modelo Car
    slug_url_kwarg = 'slug'  # nome do parâmetro na URL
    success_url = reverse_lazy('cars_urls:index')
    template_name = 'clients/client_confirm_delete.html'