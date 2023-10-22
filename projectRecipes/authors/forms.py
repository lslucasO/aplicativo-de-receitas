from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


class RegisterForm(forms.ModelForm):
    # Adicionando itens diretamente na classe super
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu nome de usuario')
        add_placeholder(self.fields['email'], 'Seu e-mail')
        add_placeholder(self.fields['first_name'], 'Ex: Lucas')
        add_placeholder(self.fields['last_name'], 'Ex: Santana')
        add_placeholder(self.fields['password'], 'Sua senha deve ser forte')
        add_attr(self.fields['username'], 'css', 'a-css-class')
        
        
    
    
    password2 = forms.CharField(
        required=True,
        widget = forms.PasswordInput(attrs={
            'placeholder': 'Sua senha',
        }),
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
        
        # help_texts = {
        #     'email': 'O e-mail precisa ser válido!',
        #     'first_name': 'teste'
        # }
        
        
        # Mensagens de erro para o usuario
        
        # error_messages = {
        #     'username': {
        #         'required': 'Esse campo é obrigatório'
        #     }
        # }
        
        # É possivel configurar os atributos do formulário também
        
        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'placeholder': 'Digite seu nome aqui...'
        #     }),

        # }
    
    
    def clean_password(self):
        # Validando campos do formulário
        data = self.cleaned_data.get('password')
        
        if 'atenção' in data:
            raise ValidationError(
                'Não digite essa palavra no formulário',
                code='invalid',
                #params={ 'value': 'atenção' }
            )
        else:
            return data  
        
        
    def clean_first_name(self):
        # Validando campos do formulário
        data = self.cleaned_data.get('first_name')
        
        if 'Lucas Santana' in data:
            raise ValidationError(
                'Não digite essa %(value)s no formulário',
                code='invalid',
                params={ 'value': '"Lucas Santana"' }
            )
        else:
            return data  
        
    
    def clean(self):
        cleaned_data = super().clean()
        
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        
        if password != password2:
            password_confirmation_error = ValidationError(
                'As suas senhas não são iguais.'
            )
            raise ValidationError(
                {
                'password': 'As senhas não são iguais',
                'password2': 'As senhas não são iguais',
                }
            )
    