from django import forms
from django.contrib.auth.forms import UserCreationForm
from dal import autocomplete

from .models import Transaction, Customer, Bike, MerchTransaction, Item, TransactionItem


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
        exclude = ('customer', 'bike', 'repairs', 'items', 'description', 'is_complete')


class MerchTransactionForm(forms.ModelForm):

    class Meta:
        model = MerchTransaction
        exclude = ('customer', 'items', 'description')


class BikeForm(forms.ModelForm):
    make = forms.CharField(label="Make", required=True)
    model = forms.CharField(label="Model", required=True)
    description = forms.CharField(label="Bike description", required=True)

    class Meta:
        model = Bike
        fields = ('make', 'model', 'description')


class AddItemToTransactionForm(forms.ModelForm):

    class Meta:
        model = TransactionItem
        fields = ('items',)
        widgets = {
            'items': autocomplete.ModelSelect2Multiple(url='item-autocomplete')
        }

