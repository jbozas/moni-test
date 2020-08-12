from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.urls import reverse
from django.shortcuts import render



class Loan(models.Model):
    amount = models.IntegerField()
    requested_date = models.DateTimeField(default=timezone.now)
    #dni = models.ForeignKey(UserRegistered, on_delete=models.CASCADE)
    gender_options = (('M', 'Male'),
                      ('F', 'Female'),
                      ('Other', 'Other'))
    DNI = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)])
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    gender = models.CharField(
        max_length=10, choices=gender_options, default="Other")

    def get_absolute_url(self):
        return reverse('loan-detail', kwargs={'pk': self.pk})


class UserRegistered(models.Model):
    gender_options = [("M", 'Male'),
                      ("F", 'Female'),
                      ("Other", 'Other')]
    dni = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)])
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    gender = models.CharField(
        max_length=10, choices=gender_options, default="Other")
