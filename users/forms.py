from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            'Usuário ou senha inválidos. Verifique os dados e tente novamente.'
        )
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'text-input',
            'placeholder': 'Digite seu usuário',
            'autocomplete': 'username',
            'autofocus': True,
        })

        self.fields['password'].widget.attrs.update({
            'class': 'text-input',
            'placeholder': '••••••••',
            'autocomplete': 'current-password',
        })

        self.fields['username'].label = 'Usuário'
        self.fields['password'].label = 'Senha'

        self.fields['username'].error_messages = {
        'required': 'Por favor, informe o seu nome usuário.',
        }

        self.fields['password'].error_messages = {
            'required': 'Por favor, digite a sua senha.',
        }

class CustomRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # LABELS
        self.fields['username'].label = 'Usuário'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme a Senha'

        #WIDGETS (INPUT EM SI)
        self.fields['username'].widget.attrs.update({
            'class': 'text-input',
            'placeholder': 'Escolha um nome de usuário',
            'autofocus': True,
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'text-input',
            'placeholder': 'Crie uma senha forte',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'text-input',
            'placeholder': 'Repita a senha',
        })

        #MENSAGENS DE ERRO

        self.fields['username'].error_messages.update({
            'required': 'Por favor, informe um nome de usuário.',
            'invalid': 'Insira um nome de usuário válido (letras, números e @/./+/-/_ apenas).',
            'unique': 'Este nome de usuário já está em uso. Escolha outro.',
        })

        self.fields['password1'].error_messages.update({
            'required': 'Por favor, digite uma senha.',
        })

        self.fields['password2'].error_messages.update({
            'required': 'Por favor, confirme a sua senha.',
        })