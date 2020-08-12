from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    document = forms.IntegerField(validators=[MaxValueValidator(99999999)])
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    gender_options = (('M', 'Male'),
                      ('F', 'Female'),
                      ('Other', 'Other'))
    gender = forms.ChoiceField(choices=gender_options)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'document', 'gender',
                  'email', 'username', 'password1', 'password2']
