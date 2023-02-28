from django.db import models

class Hostel (models.Model):
    h_num = models.CharField(max_length=4)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
      

    def __str__(self):
        return 'Hostel ' + self.h_num

class Database (models.Model):
    rollnum_1 = models.CharField(max_length=20)
    rollnum_2 = models.CharField(max_length=20)
    name_1 = models.CharField(max_length=100)
    name_2 = models.CharField(max_length=100)
    in_time = models.BooleanField()
    out_time = models.BooleanField()

class users(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.CharField(max_length=20)
    hostel_no=models.IntegerField(max_length=2)
    room_no=models.IntegerField(max_length=3)
    
    hostel_visited = models.ForeignKey(Hostel, on_delete=models.CASCADE)


def __str__(self):
    return self.name

def __str__(self):
    return self.roll_no

def __str__(self):
    return self.hostel_no

def __str__(self):
    return self.room_no

def __str__(self):
    return self.hostelvisited




