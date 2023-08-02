from django.views.generic import ListView, FormView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from rents.models import Rent
from .forms import rentForm

# Create your views here.
class RentListView(ListView):
    model = Rent
    queryset = Rent.objects.all()
    template_name = "rents/rent_list.html"
    paginate_by = 4

class RentCreateView(FormView):
    template_name = 'rents/rent_form.html'
    form_class = rentForm
    success_url = reverse_lazy('rents_urls:list')

    def form_valid(self, form):
        form.save()  # Salva o objeto Rent no banco de dados
        return super().form_valid(form)

class RentUpdateView(UpdateView):
    model = Rent
    form_class = rentForm
    template_name = 'rents/rent_form.html'
    success_url = reverse_lazy('rents_urls:list')

class RentDetailView(DetailView):
    model = Rent
    queryset = Rent.objects.all()

class RentDeleteView(DeleteView):
    model = Rent
    slug_field = 'slug'  # campo de slug no modelo Rent
    slug_url_kwarg = 'slug'  # nome do parâmetro na URL
    success_url = reverse_lazy('cars_urls:index')
    template_name = 'rents/rent_confirm_delete.html'

