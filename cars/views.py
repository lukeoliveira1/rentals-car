from django.shortcuts import render
from django.urls import reverse_lazy
from cars.models import Car
from .forms import carForm

from django.views.generic import ListView, FormView, UpdateView, DetailView, DeleteView

# Create your views here.
def index(request):
    produtos = Car.objects.all()
    return render(request, "index.html", context={'produtos': produtos})

class CarListView(ListView):
    model = Car
    queryset = Car.objects.all()
    template_name = "cars/car_list.html"
    paginate_by = 4
    
class CarCreateView(FormView):
    template_name = 'cars/car_form.html'
    form_class = carForm
    success_url = reverse_lazy('cars_urls:index')

    def form_valid(self, form):
        form.save()  # Salva o objeto Car no banco de dados
        return super().form_valid(form)

class CarUpdateView(UpdateView):
    model = Car
    form_class = carForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('cars_urls:list')

class CarDetailView(DetailView):
    model = Car
    queryset = Car.objects.all()

class CarDeleteView(DeleteView):
    model = Car
    slug_field = 'slug'  # campo de slug no modelo Car
    slug_url_kwarg = 'slug'  # nome do parâmetro na URL
    success_url = reverse_lazy('cars_urls:index')
    template_name = 'cars/car_confirm_delete.html'