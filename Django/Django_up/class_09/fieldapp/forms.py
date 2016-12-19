from .models import AddPdfFileModel
from django import forms

class AddPdfForm(forms.ModelForm):
    class Meta:
        model = AddPdfFileModel
        fields = ['name', 'file']
