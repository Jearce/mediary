from django.db import models

class Person(models.Model):
    '''
    Parent class Employee,Traveler, and InstituteFaculty.

    '''

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    passport  = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=12)

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name + " " + self.last_name

class Employee(Person):
    '''Employee table'''
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.IntegerField(max_length=12)
    email = models.EmailField(max_length=50)
    passport_number = models.IntegerField(max_length=11)


class Institute(models.Model):
    '''
    Institute can make many bookings and a booking
    will be for one trip.

    '''
    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=80)
    city_address = models.CharField(max_length=80)
    state_address = models.CharField(max_length=80)
    country_address = models.CharField(max_length=80)
    institute_type = models.CharField(max_length=80)
    student_count = models.IntegerField()

    def __str__(self):
        return self.name


class InstituteType(models.Model):
    '''
    Axiliary table for Institute model.

    '''
    institute_type = models.CharField(max_length=80)

    def __str__(self):
        return self.institute_type


class Trip(models.Model):
    '''
    Trip can have many bookings for it and that booking
    is made by an institute.

    '''
    name = models.CharField(max_length=50)
    trip_organizer = models.ForeignKey(Employee,on_delete=models.CASCADE)
    trip_expense = models.DecimalField(max_digits=6,decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    institutes = models.ManyToManyField(Institute,through="Booking")

    def __str__(self):
        return self.name


class TripExpense(models.Model):

    amount = models.DecimalField()
    date = models.DateTimeField()
    reason = models.ForeignKey(ExpenseType,on_delete=models.CASCADE)
    


class ExpenseType(models.Model):
    '''
    Axiliary table for TripExpense Model.

    '''

    expense_type = models.CharField(max_length=80)

    def __str__(self):
        return self.expense_type


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

    def __str__(self):
        return self.plan

class Invoice(models.Model):
    '''
    Many invoices can be made for a trip.

    '''
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    total_amount = models.FloatField()
    paid = models.BooleanField()
    status = model.ForeignKey(Status, on_delete=models.CASCADE)
    payment_plan = models.ForeignKey(PaymentPlan,on_delete=models.CASCADE)



class Status(models.Model):
    '''
    Axiliary table for Payment model.

    '''
    status = models.CharField(max_length=80)

    def __str__(self):
        return self.status


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
    name = models.CharField(max_length=120)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Traveler(Person):
    '''
    A trip can have many travelers who register for the trip.

    '''
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    trips = models.ManyToManyField(Trip,through="TripRegistration")
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.IntegerField(max_length=12)
    passport_number = models.IntegerField(max_length=11)
    email = models.EmailField(max_length=50)



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
    travler = models.ForeignKey(Traveler,on_delete=models.CASCADE)


class Department(models.Model):
    '''
    Axiliary table for institute facultu model.

    '''

    name = models.CharField(max_length=80)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class InstituteFaculty(Person):
    '''
    Child model of traveler

    '''
    traveler = models.OneToOneField(Traveler,on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)


class Majors(models.Model):
    '''
    Axiliary table for student model.

    '''
    major =  models.CharField(max_length=80)


class GradeLevel(models.Model):
    ''' abstracted the grade_level array into another table to meet min table quota '''
    title = models.CharField(max_length=20)
    min_credits = models.IntegerField()
    max_credits = models.IntegerField()

    def __str__(self):
        return self.title

    def __str__(self):
        return self.major


class Student(Person):
    '''
    Child model of traveler.

    '''

    '''years_in_school = [
        ('FR','Freshman'),
        ('SO','Sophomore'),
        ('JR','Junior'),
        ('SR','Senior'),
        ('GR','Graduate')
    ]'''

    traveler = models.OneToOneField(Traveler,on_delete=models.CASCADE)
    declared_major = models.ForeignKey(Majors,on_delete=models.CASCADE)
    '''grade_level = models.CharField(max_length=2,choices=years_in_school)'''
    grade_level = models.ForeignKey(GradeLevel,on_delete=models.CASCADE)
