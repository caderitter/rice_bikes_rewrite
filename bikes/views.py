from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse

from dal import autocomplete

from .forms import CustomerForm, TransactionForm, BikeForm, MerchTransactionForm
from .models import Customer, Transaction, Bike, MerchTransaction, Item, Repair


# Generic index view to list transactions on main page.
class IndexView(generic.ListView):
    template_name = 'bikes/index.html'
    context_object_name = 'transaction_list'

    def get_queryset(self):
        return Transaction.objects.order_by('-creation_date')


# Generic detail view for repair transactions.
class DetailView(generic.DetailView):
    model = Transaction
    template_name = 'bikes/repair_detail.html'


# Generic detail view for merch transactions.
class MerchDetailView(generic.DetailView):
    model = MerchTransaction
    template_name = 'bikes/merch_detail.html'


# Generic delete view for repair transactions.
class TransactionDelete(generic.DeleteView):
    model = Transaction
    success_url = reverse_lazy('index')


# Generic delete view for merch transactions.
class MerchTransactionDelete(generic.DeleteView):
    model = MerchTransaction
    # FIXME so I redirect to the past transactions list when that's implemented
    success_url = reverse_lazy('index')
    template_name = 'bikes/merch_transaction_confirm_delete.html'


# Generic update view for updating transactions - just for updating the description.
class TransactionUpdate(generic.UpdateView):
    model = Transaction
    fields = ['description']
    template_name_suffix = '_edit'


# View for adding a new repair transaction.
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
            return HttpResponseRedirect(reverse_lazy('detail', args=[new_transaction.id]))

    else:
        customer_form = CustomerForm(instance=Customer())
        transaction_form = TransactionForm(instance=Transaction())
    return render(request, 'bikes/new_repair_transaction.html',
                  {'customer_form': customer_form, 'transaction_form': transaction_form})


# View for adding a new merch transaction.
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
        transaction_form = MerchTransactionForm(instance=MerchTransaction())
    return render(request, 'bikes/new_merch_transaction.html',
                  {'customer_form': customer_form, 'transaction_form': transaction_form})


# View for adding a bike to repair transaction.
def add_bike(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.save()
    if request.method == "POST":
        bike_form = BikeForm(request.POST, instance=Bike())
        if bike_form.is_valid():
            new_bike = bike_form.save()
            transaction.bike = new_bike
            transaction.save()
            return HttpResponseRedirect(reverse_lazy('detail', args=[transaction.id]))
    else:
        bike_form = BikeForm(instance=Bike())
    return render(request, 'bikes/add_bike.html', {'bike_form': bike_form})


# View for editing a bike tied to a repair transaction.
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


# View for adding an item to a repair or merch transaction.
def add_item_to_transaction(transaction_id, item):
    t = Transaction.objects.get(id=transaction_id)
    i = Item.objects.get(name=item)
    t.entry_set.add(i)
    t.save()


# View for adding a repair to a repair transaction.
def add_repair_to_transaction(transaction_id, repair):
    t = Transaction.objects.get(id=transaction_id)
    r = Repair.objects.get(name=repair)
    t.entry_set.add(r)
    t.save()


class ItemAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        items = Item.objects.all()
        return items
