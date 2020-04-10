from django.db import models

# Create your models here.

class Person(models.Model):

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    passport  = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=12)


    class Meta:
        abstract = True



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
    city_address = model.CharField(max_length=80)
    state_address = model.CharField(max_length=80)
    country_address = model.CharField(max_length=80)
    institute_type = model.CharField(max_length=80)
    student_count = model.IntergerField()

    def __str__(self):
        return self.name



class Trip(models.Model):
    '''

    '''
    name = models.CharField(max_length=120)
    trip_organizer = models.ForeignKey(Employee,on_delete=models.CASCADE)
    trip_expense = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    institutes = models.ManyToManyField(Institute,through="Booking")


    def __str__(self):
        return self.name



class Booking(models.Model):
    '''
    FK InstitueID
    FK TripID
    '''
    name = model.CharField(max_length=120)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name
