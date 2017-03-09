from django.db import models

# Bike model.


class Bike(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.make + " " + self.model


# Item model.


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Repair model.


class Repair(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    # need a "choices" dealio or just try to figure out distinction between list of repairs and
    # where actual repairs added to bikes will be stored. new instance for every new repair?
    # or just an identifier?


# Customer model.


class Customer(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.firstName + " " + self.lastName


# Transaction model. Every transaction in the app is represented as this model.
# Note the ManyToManyField, which allows for multiple repairs and items to be added to a transaction.
# Null = True for customer field in order to avoid a bug when first creating transactions.


class Transaction(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, null=True)
    bike = models.ForeignKey(Bike, blank=True, null=True)
    repairs = models.ManyToManyField(Repair, blank=True)
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return str(self.id)


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




