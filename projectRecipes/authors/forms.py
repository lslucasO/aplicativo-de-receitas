from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        # Modelo padrão de form do Django
        
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',       
        ]
        
        # Da pra mudar o nome dos labels
        
        labels = {
            'username': 'Nome de Usuário',
        }
        
        
        # Textos de ajuda para o usuario
        
        help_texts = {
            'email': 'O e-mail precisa ser válido!',
            'first_name': 'teste'
        }
        
        
        # Mensagens de erro para o usuario
        
        error_messages = {
            'username': {
                'required': 'Esse campo é obrigatório'
            }
        }
        
        # É possivel configurar os atributos do formulário também
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu nome aqui...'
            }),
            
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha aqui...'
            })
        }