# @Project:     FundConnect
# @Filename:    forms.py
# @Author:      Daksh
# @Time:        08-06-2023 01:27 pm
from django import forms
from .models import Member

# styling
# FORM_INPUT = 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500'
# FORM_SELECT = 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500'
# FORM_CHECKBOX = 'form-checkbox text-blue-500'


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('id', 'name', 'branch', 'monthly_salary', 'refund_on_exit', 'deposits', 'loan', 'share_holding', 'user')
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'branch': forms.Select(attrs={'class': 'form-select'}),
            'monthly_salary': forms.NumberInput(attrs={'class': 'form-input'}),
            'refund_on_exit': forms.NumberInput(attrs={'class': 'form-input'}),
            'deposits': forms.NumberInput(attrs={'class': 'form-input'}),
            'loan': forms.NumberInput(attrs={'class': 'form-input'}),
            'share_holding': forms.NumberInput(attrs={'class': 'form-input'}),
            'user': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
