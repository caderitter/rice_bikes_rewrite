from django.db import models

# Bike model.


class Bike(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.make + " " + self.model

    def get_absolute_url(self):
        return "/%i" % self.id


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


# Transaction model. For customers who need repairs.


class Transaction(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, null=True)
    bike = models.ForeignKey(Bike, blank=True, null=True)
    repairs = models.ManyToManyField(Repair, blank=True)
    items = models.ManyToManyField(Item, blank=True)
    description = models.CharField(max_length=300)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


# Merchandise transaction model. For customers who only buy things vs. customers who need their bike repaired.


class MerchTransaction(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, null=True)
    items = models.ManyToManyField(Item, blank=True)
    description = models.CharField(max_length=300)

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




