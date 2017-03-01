from django.contrib import admin

from .models import Transaction, Bike, Customer, Repair, Item

admin.site.register(Transaction)
admin.site.register(Bike)
admin.site.register(Customer)
admin.site.register(Repair)
admin.site.register(Item)