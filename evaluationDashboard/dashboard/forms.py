from django import forms
from .models import UploadTable


class UploadTableForm(forms.ModelForm):
    class Meta:
        model = UploadTable
        fields = ['file']

class UploadTSVForm(forms.Form):
    file = forms.FileField()

def getFileNames():
    return {i.file: i.file for i in UploadTable.objects.all()}

class FileSelectForm(forms.Form):
    fileName = forms.ChoiceField(label="", choices=getFileNames)

