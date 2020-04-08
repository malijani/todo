""" Form to control objects in todo app """
from django import forms
from .models import List

class ListForm(forms.ModelForm):
    """ ModelForm of List Model! """
    class Meta:
        model = List
        fields = ['item', 'completed']
