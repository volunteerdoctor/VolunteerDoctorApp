from django.db import models
from django.utils import timezone
# from datetime import datetime


class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    health_facility = models.CharField(max_length=100)
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Facility(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Commitment(models.Model):
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=200)
    hours = models.IntegerField(default=0)
    location = models.CharField(max_length=50)
    availability_date = models.DateTimeField(default=None)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        availability_date = str(self.availability_date)
        date_available = availability_date[:-15]
        time_available = availability_date[-14:-9]
        return self.doctor + ' - available on ' + date_available + ' for ' + str(self.hours) + ' hours, starting at ' + time_available + '.'
