from django import forms
from .models import Url

class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['name', 'original_url', 'shortned_url']
        labels = {'name':'Nome', 'original_url':'Url para encurtar', 'shortned_url':'Nova url'}