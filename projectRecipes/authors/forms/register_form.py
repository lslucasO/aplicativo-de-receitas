from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re
from utils.django_forms import *
   
   
class RegisterForm(forms.ModelForm):
    # Adicionando itens diretamente na classe super
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu nome de usuario')
        add_placeholder(self.fields['email'], 'Seu e-mail')
        add_placeholder(self.fields['first_name'], 'Ex: Lucas')
        add_placeholder(self.fields['last_name'], 'Ex: Santana')
        add_placeholder(self.fields['password'], 'Sua senha deve ser forte')
        add_placeholder(self.fields['confirm_password'], 'Repita sua senha')
        add_attr(self.fields['username'], 'css', 'a-css-class')
        

    confirm_password = forms.CharField(
        required=True,
        widget = forms.PasswordInput(attrs={
        }),
        validators=[strong_password]
    )

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
        
        # labels = {
        #     'username': 'Nome de Usuário',
        # }
        
        
        # Textos de ajuda para o usuario
        
        help_texts = {
            'password': '''
                Password must have at least one uppercase letter,
                one lowercase letter and one number. The length should be at least 8 characters.
            '''
        }
        
        # Mensagens de erro para o usuario
        
        # error_messages = {
        #     'username': {
        #         'required': 'Esse campo é obrigatório'
        #     }
        # }
        
        # É possivel configurar os atributos do formulário também
        
        widgets = {
            'first_name': forms.TextInput(attrs={
            }),
            'password': forms.PasswordInput(attrs={  
            })

        }
    
    def clean(self):
        # Validando os campos de senha, se são iguais.
        
        cleaned_data = super().clean()
        
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            password_confirmation_error = ValidationError(
                'Password must have at least one uppercase letter, '
                'one lowercase letter and one number. The length should be '
                'at least 8 characters.',
                code='invalid'
            )
            raise ValidationError(
                {
                'password': password_confirmation_error,
                },
            )
            
            
    def clean_email(self):
        # Checando se o email do usuario é unico na base de dados
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email)
        
        if exists:
            raise ValidationError(
                'User email already exists',
                code='Invalid'
            )
        else:
            return email
    
    
    # def clean_password(self):
    #     # Validando campos especificos do formulário
    #     data = self.cleaned_data.get('password')
        
    #     if 'atenção' in data:
    #         raise ValidationError(
    #             'Não digite essa palavra no formulário',
    #             code='invalid',
    #             #params={ 'value': 'atenção' }
    #         )
    #     else:
    #         return data  
        
        
    # def clean_first_name(self):
    #     # Validando campos especificos do formulário
    #     data = self.cleaned_data.get('first_name')
        
    #     if 'Lucas Santana' in data:
    #         raise ValidationError(
    #             'Não digite essa %(value)s no formulário',
    #             code='invalid',
    #             params={ 'value': '"Lucas Santana"' }
    #         )
    #     else:
    #         return data  
        

