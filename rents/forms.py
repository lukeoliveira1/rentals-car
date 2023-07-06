from .models import Rent
from django import forms
from django.forms import TextInput

class rentForm(forms.ModelForm):

    class Meta:
        model = Rent
        fields = '__all__'

        labels = {
            'pickup_date': 'Data de Retirada',
            'value': 'Valor',
            'delivery_date': 'Data de Entrega',
            'client': 'Cliente',
            'car': 'Carro',
        }

        widgets = {
            'pickup_date': forms.DateInput(
                    format = '%d/%m/%Y', 
                    attrs={
                        'type':'date',
                        'class':'form-control'
                    }
                ),
            'delivery_date': forms.DateInput(
                    format = '%d/%m/%Y', 
                    attrs={
                        'type':'date',
                        'class':'form-control'
                    }
                ),

        }