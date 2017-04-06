from django.contrib import admin

from .models import Transaction, Bike, Customer, Repair, Item, MerchTransaction

admin.site.register(Transaction)
admin.site.register(Bike)
admin.site.register(Customer)
admin.site.register(Repair)
admin.site.register(Item)
admin.site.register(MerchTransaction)