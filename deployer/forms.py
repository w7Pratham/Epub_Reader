from django import forms
from .models import EpubFile

class EpubUploadForm(forms.ModelForm):
    class Meta:
        model = EpubFile
        fields = ('title', 'epub_file')
