from .models import Car
from django.forms import ModelForm

class carForm(ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

        labels = {
            'model': 'Modelo',
            'manufacter': 'Marca',
            'color': 'Cor do Veículo',
            'year': 'Ano',
            'motor': 'Motor',
            'fuel_type': 'Tipo de Combustível',
            'license_plate': 'Placa',
        }
