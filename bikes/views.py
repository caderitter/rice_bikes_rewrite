from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import CustomerForm, TransactionForm, BikeForm, MerchTransactionForm
from .models import Customer, Transaction, Bike, MerchTransaction


class IndexView(generic.ListView):
    template_name = 'bikes/index.html'
    context_object_name = 'transaction_list'

    def get_queryset(self):
        return Transaction.objects.order_by('-creation_date')


class DetailView(generic.DetailView):
    model = Transaction
    template_name = 'bikes/repair_detail.html'


class MerchDetailView(generic.DetailView):
    model = MerchTransaction
    template_name = 'bikes/merch_detail.html'


class TransactionDelete(generic.DeleteView):
    model = Transaction
    success_url = reverse_lazy('index')


class MerchTransactionDelete(generic.DeleteView):
    model = MerchTransaction
    #FIXME so I redirect to the past transactions list
    success_url = reverse_lazy('index')
    template_name = 'bikes/merch_transaction_confirm_delete.html'


class BikeUpdate(generic.UpdateView):
    model = Transaction.bike
    fields = ['make', 'model', 'description']
    template_name_suffix = '_edit'


class TransactionUpdate(generic.UpdateView):
    model = Transaction
    fields = ['description']
    template_name_suffix = '_edit'


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
    return render(request, 'bikes/new_repair_transaction.html',
                  {'customer_form': customer_form, 'transaction_form': transaction_form})


def add_merch_transaction(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST, instance=Customer())
        transaction_form = MerchTransactionForm(request.POST, instance=MerchTransaction())
        if customer_form.is_valid() and transaction_form.is_valid():
            new_customer = customer_form.save()
            new_transaction = transaction_form.save()
            new_transaction.customer = new_customer
            new_transaction.save()
            return HttpResponseRedirect(reverse_lazy('merch_detail', args=[new_transaction.id]))

    else:
        customer_form = CustomerForm(instance=Customer())
        transaction_form = TransactionForm(instance=MerchTransaction())
    return render(request, 'bikes/new_merch_transaction.html',
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


def edit_bike(request, pk):
    this_transaction = Transaction.objects.get(pk)
    this_bike = this_transaction.bike
    if request.method == "POST":
        edit_bike_form = BikeForm(request.POST, instance=Bike(this_bike))
        if edit_bike_form.is_valid():
            this_bike = edit_bike_form.save()
            this_transaction.bike = this_bike
            this_transaction.save()
            return HttpResponseRedirect('/%s/' % str(this_transaction.id))
    else:
        edit_bike_form = BikeForm(instance=Bike(this_bike))
    return render(request, 'bikes/bike_edit.html', {'edit_bike_form': edit_bike_form})








