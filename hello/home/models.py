from django.db import models

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=50)
    roll_n0=models.CharField(max_length=20)
    hostel_no=models.IntegerField(max_length=2)
    room_no=models.IntegerField(max_length=3)
    hostelvisited=models.IntegerField(max_length=2)

def __str__(self):
    return self.name

def __str__(self):
    return self.roll_n0

def __str__(self):
    return self.hostel_no

def __str__(self):
    return self.room_no

def __str__(self):
    return self.hostelvisited