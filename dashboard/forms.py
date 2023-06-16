# @Project:     FundConnect
# @Filename:    forms.py
# @Author:      Daksh
# @Time:        13-06-2023 02:34 pm

from django import forms
from .models import Controller

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class ControllerForm(forms.ModelForm):
    class Meta:
        model = Controller
        fields = ('name', 'email', 'refund_on_exit_monthly_deposit', 'dividend_interest', 'pay_off_period_of_dividend',
                  'loan_interest', 'loan_interest_period', 'service_fee_interest', 'service_fee_period',
                  'loan_monthly_salary_ratio_limit', 'loan_share_holding_ratio_limit')
        labels = {"name": "Name", "email": "Email", "refund_on_exit_monthly_deposit": "NRD",
                  "dividend_interest": "Dividend Interest in %",
                  "pay_off_period_of_dividend": "Pay Off Period of Dividend in Months",
                  "loan_interest": "Loan Interest in %", "loan_interest_period": "Loan Interest Period in Months",
                  "service_fee_interest": "Service Fee Interest in %",
                  "service_fee_period": "Service Fee Period in Months",
                  "loan_monthly_salary_ratio_limit": "Loan to Salary Ratio Limit",
                  "loan_share_holding_ratio_limit": "Loan to Share Holding Ratio Limit"}
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),
            'refund_on_exit_monthly_deposit': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'dividend_interest': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'pay_off_period_of_dividend': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'loan_interest': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'loan_interest_period': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'service_fee_interest': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'service_fee_period': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'loan_monthly_salary_ratio_limit': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'loan_share_holding_ratio_limit': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }
