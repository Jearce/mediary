from django.db import models
#TODO add max_digits and decimial_places to DecimalField

class Person(models.Model):

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    passport  = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=12)


    class Meta:
        abstract = True


class Employee(Person):
    '''Employee table'''


class Institute(models.Model):
    '''

    PK instituteID
    InstituteName
    StreetAddress
    CityAddress
    StateAddress
    CountryAddress
    Type
    StudentCount

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
    institute_type = models.CharField(max_length=80)

    def __str__(self):
        return self.institute_type


class Trip(models.Model):
    '''

    '''
    name = models.CharField(max_length=50)
    trip_organizer = models.ForeignKey(Employee,on_delete=models.CASCADE)
    trip_expense = models.DecimalField()
    start_date = models.DateField()
    end_date = models.DateField()
    institutes = models.ManyToManyField(Institute,through="Booking")

    def __str__(self):
        return self.name


class TripExpense(models.Model):
    pass


class ExpenseType(models.Model):

    expense_type = models.CharField(max_length=80)

    def __str__(self):
        return self.expense_type


class RequestForProposal(models.Model):

    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    submission_date = models.DateField()
    projected_date = models.DateField()
    rfp_status = models.CharField(max_length=80)
    proposed_amount = models.DecimalField()
    accepted_amount = models.DecimalField()
    trips = models.ManyToManyField(Trip,through="Bid")

    def __str__(self):
        return self.name


class Bid(models.Model):
    '''

    '''
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    rfp = models.ForeignKey(RequestForProposal,on_delete=models.CASCADE)
    amount = models.DecimalField()
    accepted = models.BooleanField()


class PaymentPlan(models.Model):
    plan = models.CharField(max_length=80)

    def __str__(self):
        return self.plan


class Invoice(models.Model):
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    total_amount = models.FloatField()
    paid = models.BooleanField()
    payment_plan = models.ForeignKey(PaymentPlan,on_delete=models.CASCADE)


class PaymentStatus(models.Model):
    status = models.CharField(max_length=80)


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    amount = models.DecimalField()
    payment_type = models.CharField(max_length=12)
    payment_status = models.ForeignKey(PaymentStatus,on_delete=models.CASCADE)


class Booking(models.Model):
    '''
    FK InstitueID
    FK TripID
    '''
    name = models.CharField(max_length=120)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Traveler(Person):
    '''

    '''
    insitute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    trips = models.ManyToManyField(Trip,through="TripRegistration")


class TripHistory(models.Model):
    '''

    '''
    traveler  = models.ForeignKey(Traveler,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class TripRegistration(models.Model):
    '''
    Associative table for Trip and Traveler.
    '''
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    travler = models.ForeignKey(Traveler,on_delete=models.CASCADE)


class Department(models.Model):

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class InstituteFaculty(Person):
    '''

    '''
    traveler = models.ForeignKey(Traveler,on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)


class Majors(models.Model):
    '''

    '''
    major =  models.CharField(max_length=80)


class Student(Person):
    '''

    '''

    years_in_school = [
        ('FR','Freshman'),
        ('SO','Sophomore'),
        ('JR','Junior'),
        ('SR','Senior'),
        ('GR','Graduate')
    ]

    traveler = models.ForeignKey(Traveler,on_delete=models.CASCADE)
    declared_major = models.ForeignKey(Majors,on_delete=models.CASCADE)
    grade_level = models.CharField(max_length=2,choices=years_in_school)
