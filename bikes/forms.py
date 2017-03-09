from django import forms

from .models import Transaction, Customer, Bike


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


class BikeForm(forms.ModelForm):
    make = forms.CharField(label="Make", required=True)
    model = forms.CharField(label="Model", required=True)
    description = forms.CharField(label="Bike description", required=True)

    class Meta:
        model = Bike
        exclude = ('transaction',)



