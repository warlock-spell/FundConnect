# @Project:     FundConnect
# @Filename:    forms.py
# @Author:      Daksh
# @Time:        08-06-2023 01:27 pm

from django import forms
from .models import Branch

# styling
FORM_INPUT = 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500'
FORM_SELECT = 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500'
FORM_CHECKBOX = 'form-checkbox text-blue-500'


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'location', 'manager')
        widgets = {
            'name': forms.TextInput(attrs={'class': FORM_INPUT}),
            'location': forms.TextInput(attrs={'class': FORM_INPUT}),
            'manager': forms.TextInput(attrs={'class': FORM_INPUT}),
        }
