from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Transaction


class IndexView(generic.ListView):
    template_name = 'bikes/index.html'
    context_object_name = 'transaction_list'

    def get_queryset(self):
        return Transaction.objects.order_by('-creation_date')


class DetailView(generic.DetailView):
    model = Transaction
    template_name = 'bikes/detail.html'



