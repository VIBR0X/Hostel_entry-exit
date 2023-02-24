from django.db import models

class Hostel (models.Model):
    h_num = models.CharField(max_length=4)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    

    def __str__(self):
        return 'Hostel ' + self.h_num

