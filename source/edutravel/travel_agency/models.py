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
    destinations = models.IntegerField()

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

    amount = models.DecimalField()
    date = models.DateTimeField()
    reason = models.ForeignKey(ExpenseType,on_delete=models.CASCADE)
    
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

    def __str__(self):
        return self.major

class GradeLevel(models.Model):
    ''' abstracted the grade_level array into another table to meet min table quota '''
    title = models.CharField(max_length=20)
    min_credits = models.IntegerField()
    max_credits = models.IntegerField()

    def __str__(self):
        return self.title

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

class LanguageCode(models.Model):
    name = models.CharField(max_length=80)
    short_code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Country(models.Model):
    '''
    Contains the list of Counties
    '''
    name = models.CharField(max_length=80)
    latitude = models.FloatField()
    longitude = models.FloatField()
    primary_language = models.ForeignKey(LanguageCode,on_delete=models.CASCADE)
    capital = models.CharField(max_length=80)
    hemisphere = models.CharField(max_length=8)

    def __str__(self):
        return self.name

class Subdivision(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class City(models.Model):
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    Name = models.CharField()

class TripCity(models.Model):
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class ZipCode(models.Model):
    zip_code = models.IntegerField()

    def __str__(self):
        return self.zip_code

class TypeTable(models.Model):
    name = models.CharField(max_length=80)
    entity = models.CharField(max_length=80)

    def __str__(self):
        return self.name
'''
class LodgingType(models.Model):
    merged into TypeTables
'''

class LocalLodging(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    lodging_type = models.ForeignKey(TypeTable, on_delete=models.CASCADE, limit_choices_to={'entity': 'LocalLodging'})
    street_address = models.CharField(max_length=80)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name

'''
class BusinessType(models.Model):
    merged into TypeTables
'''
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

class GuideSpecialty(models.Model):
    specialty = models.CharField(max_length=80)

    def __str__(self):
        return self.specialty

class LocalGuide(Person):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    specialty = models.ForeignKey(GuideSpecialty,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

'''
class transportationType(models.Model):
    merged into TypeTables
'''
class LocalTransportation(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    open_time = models.TimeField()
    close_time = models.TimeField()
    type = models.ForeignKey(TypeTable,on_delete=models.CASCADE, limit_choices_to={'entity':'LocalTransportation'})

class Itinerary(models.Model):
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    lodging = models.ForeignKey(LocalLodging, on_delete=models.CASCADE)
    first_destination = models.ManyToManyField(LocalAttraction, through="AttractionDestination")
    first_destination_start_time = models.DateTimeField()
    first_destination_end_time = models.DateTimeField()
    second_destination = models.ManyToManyField(LocalAttraction, through="AttractionDestination")
    second_destination_start_time = models.DateTimeField()
    second_destination_end_time = models.DateTimeField()
    third_destination = models.ManyToManyField(LocalAttraction, through="AttractionDestination")
    third_destination_start_time = models.DateTimeField()
    third_destination_end_time = models.DateTimeField()

class AttractionDestination(models.Model):
    itenerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    local_attraction = models.ForeignKey(LocalAttraction, on_delete=models.CASCADE)