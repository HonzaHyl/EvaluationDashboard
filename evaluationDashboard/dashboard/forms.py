from django import forms
from .models import UploadTable

class UploadTableForm(forms.ModelForm):
    class Meta:
        model = UploadTable
        fields = ['file']