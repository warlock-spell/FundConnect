# @Project:     FundConnect
# @Filename:    forms.py
# @Author:      Daksh
# @Time:        08-06-2023 01:27 pm
from django import forms
from .models import Member
from branch.models import Branch

# styling
# FORM_INPUT = 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500'
# FORM_SELECT = 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500'
# FORM_CHECKBOX = 'form-checkbox text-blue-500'
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
SEARCH_INPUT_CLASSES = 'w-full py-2 px-4 border'


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = (
            'id', 'name', 'branch', 'position', 'monthly_salary', 'wish_to_deposit', 'refund_on_exit',
            'deposits',
            'loan',
            'share_holding')
        widgets = {
            'id': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'branch': forms.Select(attrs={'class': INPUT_CLASSES}),
            'position': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'monthly_salary': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'wish_to_deposit': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'refund_on_exit': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'deposits': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'loan': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'share_holding': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
        }


class EditMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = (
            'id', 'name', 'branch', 'position', 'monthly_salary', 'wish_to_deposit', 'refund_on_exit',
            'deposits',
            'loan',
            'share_holding', 'active_user')
        widgets = {
            'id': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'branch': forms.Select(attrs={'class': INPUT_CLASSES}),
            'position': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'monthly_salary': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'wish_to_deposit': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'refund_on_exit': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'deposits': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'loan': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'share_holding': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'active_user': forms.CheckboxInput(attrs={'class': INPUT_CLASSES}),
        }


class MemberSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False,
                                   widget=forms.TextInput(
                                       attrs={'placeholder': 'Enter name or Membership No.',
                                              'class': SEARCH_INPUT_CLASSES}))
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), empty_label='All Branches', required=False,
                                    widget=forms.Select(attrs={'class': SEARCH_INPUT_CLASSES}))
