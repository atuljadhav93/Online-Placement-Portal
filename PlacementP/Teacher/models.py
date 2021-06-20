from django.db import models

# Create your models here.

class Teacher(models.Model):
    gnd = (
        ('M','Male'),
        ('F','Female'),
        ('T','Transgender')
    )
    FirstName = models.CharField(max_length=100)
    MiddleName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Mobile = models.BigIntegerField()
    AlternateMobile = models.BigIntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Gender = models.CharField(max_length=1,choices=gnd)
    DateOfBirth = models.DateField()
    Photo = models.ImageField(upload_to='ProfilePhotos')
    Course = models.CharField(max_length=200)
    IsAdmin = models.BooleanField()















