# @Project:     FundConnect
# @Filename:    forms.py
# @Author:      Daksh
# @Time:        08-06-2023 01:27 pm

from django import forms
from .models import Branch

# styling
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'location', 'manager')
        labels = {'name': 'Name', 'location': 'Location', 'manager': 'Manager'}
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'location': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'manager': forms.TextInput(attrs={'class': INPUT_CLASSES}),
        }


class EditBranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'location', 'manager')
        labels = {'name': 'Name', 'location': 'Location', 'manager': 'Manager'}
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'location': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'manager': forms.TextInput(attrs={'class': INPUT_CLASSES}),
        }
