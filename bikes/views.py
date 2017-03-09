from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import CustomerForm, TransactionForm, BikeForm
from .models import Customer, Transaction, Bike


class IndexView(generic.ListView):
    template_name = 'bikes/index.html'
    context_object_name = 'transaction_list'

    def get_queryset(self):
        return Transaction.objects.order_by('-creation_date')


class DetailView(generic.DetailView):
    model = Transaction
    template_name = 'bikes/detail.html'


class TransactionDelete(generic.DeleteView):
    model = Transaction
    success_url = reverse_lazy('index')


# Thanks to Collin Grady for help on this view.
# https://collingrady.wordpress.com/2008/02/18/editing-multiple-objects-in-django-with-newforms/
def add_transaction(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST, instance=Customer())
        transaction_form = TransactionForm(request.POST, instance=Transaction())
        if customer_form.is_valid() and transaction_form.is_valid():
            new_customer = customer_form.save()
            new_transaction = transaction_form.save()
            new_transaction.customer = new_customer
            new_transaction.save()
            return HttpResponseRedirect('/' + str(new_transaction.id) + '/')

    else:
        customer_form = CustomerForm(instance=Customer())
        transaction_form = TransactionForm(instance=Transaction())
    return render(request, 'bikes/new_transaction.html',
                  {'customer_form': customer_form, 'transaction_form': transaction_form})


def add_bike(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.save()
    if request.method == "POST":
        bike_form = BikeForm(request.POST, instance=Bike())
        if bike_form.is_valid():
            new_bike = bike_form.save()
            transaction.bike = new_bike
            transaction.save()
            return HttpResponseRedirect('/' + str(transaction.id) + '/')

    else:
        bike_form = BikeForm(instance=Bike())
        return render(request, 'bikes/add_bike.html', {'bike_form': bike_form})






