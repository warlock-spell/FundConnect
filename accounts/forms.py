# @Project:     FundConnect
# @Filename:    forms.py
# @Author:      Daksh Gaur
# @Email:       hi@daksh.fyi
# @Time:        24-06-2023 03:28 pm
from django import forms
from .models import CashBookEntry

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
SEARCH_INPUT_CLASSES = 'w-full py-2 px-4 border'


class CashBookEntryForm(forms.ModelForm):
    class Meta:
        model = CashBookEntry
        fields = (
            'date', 'month', 'year', 'fund_type', 'refund_on_exit_amount', 'deposits_amount', 'loan_amount', 'member',
        )
        widgets = {
            'date': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'month': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'year': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'fund_type': forms.Select(attrs={'class': INPUT_CLASSES}),
            'refund_on_exit_amount': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'deposits_amount': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'loan_amount': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'member': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
        }
