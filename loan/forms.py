from django import forms
from django.core.validators import MaxValueValidator


class LoanCreationForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    document = forms.IntegerField(validators=[MaxValueValidator(99999999)])
    email = forms.EmailField()
    gender_options = (('M', 'Male'),
                      ('F', 'Female'),
                      ('Other', 'Other'))
    gender = forms.ChoiceField(choices=gender_options)
    amount = forms.IntegerField(min_value=1)


# When the user is already logged, we don't need some fields
class LoanAlternCreationForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
