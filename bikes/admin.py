from django.contrib import admin

from .models import Transaction, Bike, Customer

admin.site.register(Transaction)
admin.site.register(Bike)
admin.site.register(Customer)