from contacts.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'email', 'number', 'description', 'category'
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'number': 'Número de Telefone',
            'category': 'Categoria',
            'description': 'Descrição',
            }