from .models import List
from django import forms


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('item','completed')
