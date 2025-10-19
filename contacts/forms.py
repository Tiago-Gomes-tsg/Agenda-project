from contacts.models import Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

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
        
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        label= 'Nome'
    )
    
    last_name = forms.CharField(
        required=True,
        min_length=3,
        label= 'Sobrenome'
    )
    
    email = forms.EmailField(
        required=True,
        label= 'E-mail'
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)
        
    def clean_email(self):
        email = self.cleaned_data.get( 'email')
        
        if User.objects.filter(email = email).exists():
            self.add_error(
                'email',
                error='Já exite uma conta com este endereço de email.'
            )
        return email
    
class RegisterUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)
        
    def clean_email(self):
        email = self.cleaned_data.get( 'email')
        current_email = self.instance.email 
        
        if current_email != email:
            if User.objects.filter(email = email).exists():
                self.add_error(
                    'email',
                    error='Já exite uma conta com este endereço de email.'
                )
            return email
    
    def clean_password1(self):
        password1= self.cleaned_data.get('password1')
        
        if password1:
            try:
                password_validation.validate_password(password1)
            
            except ValidationError as errors:
                ...
                
        
        return password1