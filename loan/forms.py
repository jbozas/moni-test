from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator


class LoanCreationForm(UserCreationForm):
    email = forms.EmailField()
    document = forms.IntegerField(validators=[MaxValueValidator(99999999)])
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    gender_options = (('M', 'Male'),
                      ('F', 'Female'),
                      ('Other', 'Other'))
    gender = forms.ChoiceField(choices=gender_options)

    class Meta:
        model = User
        if(user.is_authenticated):
          fields = ['first_name'=user.name, 'last_name'=user.last_name, 'document'=user.document, 'gender',
                  'email', 'username', 'password1', 'password2']
        else:
          fields = ['first_name', 'last_name', 'document', 'gender',
                  'email', 'username', 'password1', 'password2']

