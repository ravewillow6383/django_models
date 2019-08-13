from django.db import models

# Create your models here.
class Passenger(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Seats(models.Model):
    seatnumber = models.CharField(max_length=3)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

