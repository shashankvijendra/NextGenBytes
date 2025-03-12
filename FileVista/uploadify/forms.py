# forms.py

from django import forms
from .models import File, Modification

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']

class ModificationForm(forms.ModelForm):
    class Meta:
        model = Modification
        fields = ['change_description']
