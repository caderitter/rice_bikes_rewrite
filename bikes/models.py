from django.db import models


# Bike model.


class Bike(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)


# Repair model.


class Repair(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    cost = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    # need a "choices" dealio or just try to figure out distinction between list of repairs and
    # where actual repairs added to bikes will be stored. new instance for every new repair?
    # or just an identifier?


# Item model.


class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    cost = models.IntegerField(default=0)


# Customer model.


class Customer(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=30)


# Transaction model. Every transaction in the app is represented as this model.
# Note the ManyToManyField, which allows for multiple repairs and items to be added to a transaction.


class Transaction(models.Model):
    creation_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, blank=True, null=True)
    repairs = models.ManyToManyField(Repair, blank=True)
    items = models.ManyToManyField(Item, blank=True)


# Refurb model.


class Refurb(models.Model):
    creation_date = models.DateField()
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    repairs = models.ManyToManyField(Repair, blank=True)
    items = models.ManyToManyField(Item, blank=True)


# Rental model.


class Rental(models.Model):
    rental_number = models.IntegerField(default=0)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    transactions = models.ManyToManyField(Transaction, blank=True)




