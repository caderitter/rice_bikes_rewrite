from django import forms
import datetime
from .models import Transaction, Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('email', 'firstName', 'lastName')


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ('customer', 'bike', 'repairs', 'items',)


