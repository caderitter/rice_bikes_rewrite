from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
import datetime

from .forms import CustomerForm, TransactionForm
from .models import Customer, Transaction

class IndexView(generic.ListView):
    template_name = 'bikes/index.html'
    context_object_name = 'transaction_list'

    def get_queryset(self):
        return Transaction.objects.order_by('-creation_date')


class DetailView(generic.DetailView):
    model = Transaction
    template_name = 'bikes/detail.html'


def add_transaction(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST, instance=Customer())
        transaction_form = TransactionForm(request.POST, instance=Transaction())
        if customer_form.is_valid() and transaction_form.is_valid():
            new_customer = customer_form.save()
            new_transaction = transaction_form.save()
            new_transaction.customer = new_customer
            new_transaction.save()
            return HttpResponseRedirect('/')
    else:
        customer_form = CustomerForm(instance=Customer())
        transaction_form = TransactionForm(instance=Transaction())
    return render(request, 'bikes/new_transaction.html', {'customer_form': customer_form, 'transaction_form': transaction_form})





