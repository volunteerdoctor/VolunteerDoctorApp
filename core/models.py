from django.db import models
from django.utils import timezone


class Medic(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    health_facility = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    email = models.EmailField()
    # password = models.PasswordField()
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


class Request(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Commitment(models.Model):
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE)
    hours = models.IntegerField(default=0)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    availability_date = models.DateTimeField(default=None)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        availability_date = str(self.availability_date)
        date_available = availability_date[:-15]
        time_available = availability_date[-14:-9]
        return self.medic.__str__() + ' - available on ' + date_available + ' for ' + str(self.hours) + ' hours, starting at ' + time_available + '.'
