from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import Institute,Traveler


class Person(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    passport  = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=12)

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name + " " + self.last_name

class Country(models.Model):
    '''
    Contains the list of Counties
    '''
    name = models.CharField(max_length=80)
    capital = models.CharField(max_length=80)
    currency = models.CharField(max_length=8)

    def __str__(self):
        return self.name

class Subdivision(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class City(models.Model):
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    latitude = models.FloatField()
    logitude = models.FloatField()
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class ZipCode(models.Model):
    zip_code = models.CharField(max_length=80)

    def __str__(self):
        return self.zip_code

class TypeTable(models.Model):
    name = models.CharField(max_length=80)
    entity = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class LocalLodging(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    lodging_type = models.ForeignKey(TypeTable, on_delete=models.CASCADE, limit_choices_to={'entity': 'LocalLodging'})
    street_address = models.CharField(max_length=80)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name

class Industry(models.Model):
    industry = models.CharField(max_length=80)

    def __str__(self):
        return self.industry

class LocalAttraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    business_type = models.ForeignKey(TypeTable, on_delete=models.CASCADE, limit_choices_to={'entity': 'LocalBusiness'})
    name = models.CharField(max_length=80)
    industry = models.ForeignKey(Industry,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=80)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE)
    is_active = models.BooleanField(default='true')

    def __str__(self):
        return self.name

class GuideSpecialty(models.Model):
    specialty = models.CharField(max_length=80)

    def __str__(self):
        return self.specialty

class LocalGuide(Person):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    specialty = models.ForeignKey(GuideSpecialty,on_delete=models.CASCADE)

class LocalTransportation(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    open_time = models.TimeField()
    close_time = models.TimeField()
    transport_type = models.ForeignKey(TypeTable,on_delete=models.CASCADE, limit_choices_to={'entity':'LocalTransportation'})

class Employee(Person):
    '''Employee table'''

class Trip(models.Model):
    '''
    Trip can have many bookings for it and that booking
    is made by an institute.

    '''
    name = models.CharField(max_length=50)
    trip_organizer = models.ForeignKey(Employee,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    lodging = models.ForeignKey(LocalLodging,on_delete=models.CASCADE)
    institutes = models.ManyToManyField(Institute,through="Booking")
    destinations = models.ManyToManyField(LocalAttraction,through="TripDestinations")
    travelers = models.ManyToManyField(Traveler,through="TripRegistration")

    def __str__(self):
        return self.name

class ExpenseType(models.Model):
    '''
    Axiliary table for TripExpense Model.

    '''
    expense_type = models.CharField(max_length=80)

    def __str__(self):
        return self.expense_type

class TripExpense(models.Model):

    amount = models.DecimalField(max_digits=6,decimal_places=2)
    date = models.DateTimeField()
    reason = models.ForeignKey(ExpenseType,on_delete=models.CASCADE)

    def __str__(self):
        return self.amount

class RequestForProposal(models.Model):
    '''
    Many request for proposals (RFP) can be
    submitted by an institute. An RFP can have
    many bids for a trip.

    '''

    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    submission_date = models.DateField()
    projected_date = models.DateField()
    rfp_status = models.CharField(max_length=80)
    proposed_amount = models.DecimalField(max_digits=6,decimal_places=2)
    accepted_amount = models.DecimalField(max_digits=6,decimal_places=2)
    trips = models.ManyToManyField(Trip,through="Bid")

    def __str__(self):
        return self.name

class Bid(models.Model):
    '''
    Associative table

    A request for proposal can have many bids for it and a bid will
    be made for a trip.

    '''
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    rfp = models.ForeignKey(RequestForProposal,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    accepted = models.BooleanField()

class PaymentPlan(models.Model):
    '''
    Axiliary table for Invoice model.

    '''
    plan = models.CharField(max_length=80)
    number_of_payments = models.IntegerField()


    def __str__(self):
        return self.plan

class Status(models.Model):
    '''
    Axiliary table for Payment model.

    '''
    status = models.CharField(max_length=80)

    def __str__(self):
        return self.status

class Invoice(models.Model):
    '''
    Many invoices can be made for a trip.

    '''
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    total_amount = models.FloatField()
    paid = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    payment_plan = models.ForeignKey(PaymentPlan,on_delete=models.CASCADE)

class Payment(models.Model):
    '''
    An invoice can have many payments.

    '''
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    payment_type = models.CharField(max_length=12)
    payment_status = models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__(self):
        return self.amount

class Booking(models.Model):
    '''

    Associative table

    A booking belongs to a trip.

    '''
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TripHistory(models.Model):
    '''
    A traveler will have a history of their trips.

    '''
    traveler  = models.ForeignKey(Traveler,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class TripRegistration(models.Model):
    '''
    Associative table for Trip and Traveler.

    A traveler can make many registrations and a registration will be
    for a trip.

    '''
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    traveler = models.ForeignKey(Traveler,on_delete=models.CASCADE)

class TripDestinations(models.Model):
    local_attraction = models.ForeignKey(LocalAttraction,on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

