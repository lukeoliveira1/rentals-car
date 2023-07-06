from django import forms
from django.forms.models import ModelForm
from .models import Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class clientForm(ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
	
        labels = {
            'name': 'Nome',
            'cpf': 'CPF',
            'cnh': 'CNH',
            'email': 'E-mail',
            'phone_number': 'Telefone',
            'address': 'Endereço',
        }
