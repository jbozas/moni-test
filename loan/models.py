from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.urls import reverse
from django.shortcuts import render


class Loan(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    requested_date = models.DateTimeField(default=timezone.now)
    document = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999999)])
    approved = models.BooleanField()
    gender_options = (('M', 'Male'),
                      ('F', 'Female'),
                      ('Other', 'Other'))
    email = models.EmailField(max_length=254, default='none@gmail.com')
    gender = models.CharField(
        max_length=10, choices=gender_options, default="Other")
    amount = models.IntegerField()

    def get_absolute_url(self):
        return reverse('loan-detail', kwargs={'pk': self.pk})
