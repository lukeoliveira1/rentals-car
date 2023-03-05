from .models import aluguel
from django.forms import ModelForm

class aluguelForm(ModelForm):

    class Meta:
        model = aluguel
        fields = '__all__'
