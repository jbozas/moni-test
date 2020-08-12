from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Profile(models.Model):

    document = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)])
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender_options = (('M', 'Male'),
                      ('F', 'Female'),
                      ('Other', 'Other'))
    email = models.EmailField(max_length=254)
    gender = models.CharField(
        max_length=10, choices=gender_options, default="Other")

    def __str__(self):
        return f'{self.user.username} Profile'

