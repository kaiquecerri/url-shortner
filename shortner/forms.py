from django import forms
from .models import Url

class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['name', 'original_url', 'shortned_url']
        labels = {'name':'Nome', 'original_url':'Url para encurtar', 'shortned_url':'Nova url'}
        error_messages = {
            'shortned_url':{
                'unique':'Essa abreviação já foi utilizada.'
            }
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'text-input'}),
            'original_url':forms.TextInput(attrs={'class':'text-input'}),
            'shortned_url':forms.TextInput(attrs={'class':'text-input'}),
        }