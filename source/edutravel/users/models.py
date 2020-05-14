from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_institute = models.BooleanField(default=False)

class InstituteType(models.Model):
    '''
    Axiliary table for Institute model.

    '''
    institute_type = models.CharField(max_length=80)

    def __str__(self):
        return self.institute_type

class Institute(models.Model):
    '''
    Institute can make many bookings and a booking
    will be for one trip.

    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    street_address = models.CharField(max_length=80)
    city_address = models.CharField(max_length=80)
    state_address = models.CharField(max_length=80)
    country_address = models.CharField(max_length=80)
    institute_type = models.ForeignKey(InstituteType,on_delete=models.CASCADE)

class Traveler(models.Model):
    '''
    A trip can have many travelers who register for the trip.

    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)

class Department(models.Model):
    '''
    Axiliary table for institute faculty model.

    '''
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class InstituteFaculty(models.Model):
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

class Student(models.Model):
    '''
    Child model of traveler.

    '''

    traveler = models.OneToOneField(Traveler,on_delete=models.CASCADE)
    declared_major = models.ForeignKey(Majors,on_delete=models.CASCADE)
    grade_level = models.ForeignKey(GradeLevel,on_delete=models.CASCADE)
