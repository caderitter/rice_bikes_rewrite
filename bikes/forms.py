from django import forms
import datetime
from .models import Transaction, Customer


class CustomerForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    firstName = forms.CharField(label="First name", required=True)
    lastName = forms.CharField(label="Last name", required=True)

    class Meta:
        model = Customer
        fields = ('email', 'firstName', 'lastName')


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        exclude = ('customer', 'bike', 'repairs', 'items',)


