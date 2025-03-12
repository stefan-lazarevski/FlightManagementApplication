from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Airline(models.Model):
    name = models.CharField(max_length=50)
    year_founded = models.IntegerField()
    outside_of_Europe = models.BooleanField()

    def __str__(self):
        return self.name

class Balloon(models.Model):
    type = [
        ("S", "Small Balloon"),
        ("M", "Medium Balloon"),
        ("L", "Large Balloon"),
    ]

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=type)
    manufacturer = models.CharField(max_length=100)
    max_passengers = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class Pilot(models.Model):
    rank = [
        ("J", "Junior"),
        ("I", "Intermediate"),
        ("S", "Senior")
    ]

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    total_flight_hours = models.IntegerField()
    rank = models.CharField(max_length=1, choices=rank)

    def __str__(self):
        return f"{self.name} {self.lastname} ({self.get_rank_display()})"

class AirLinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.airline} {self.pilot}"

class Flight(models.Model):
    code = models.CharField(max_length=10, unique=True)
    take_off_airport = models.CharField(max_length=50)
    landing_airport = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='flight_photos/', null=True, blank=True)
    date = models.DateField()
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"Flight {self.code} ({self.take_off_airport} to {self.landing_airport})"
