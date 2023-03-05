from .models import carro
from django.forms import ModelForm

class carroForm(ModelForm):

    class Meta:
        model = carro
        fields = '__all__'
