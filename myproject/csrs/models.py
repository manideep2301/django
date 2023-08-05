from django.contrib.auth.models import User
from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class StudentRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('waitlist', 'Waitlist')])

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
