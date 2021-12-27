from django import forms

from .models import FileDetails


class FileForm(forms.ModelForm):
    class Meta:
        model = FileDetails
        fields = ('username','fileupl',)
    