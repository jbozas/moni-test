from django.shortcuts import render, redirect
from .models import Loan
from .verification import ItsApproved
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoanCreationForm
from django.views.generic import (CreateView,
                                  DetailView)


def home(request):
    return render(request, 'loan/home.html')


def about(request):
    return render(request, 'loan/about.html')


def NewLoan(request):
    if request.method == 'POST':
        form = LoanCreationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            document = form.cleaned_data.get('document')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            amount = form.cleaned_data.get('amount')
            approved = ItsApproved(document)
            print(approved)
            loan = Loan(document=document, first_name=first_name, last_name=last_name,
                        email=email, gender=gender, approved=approved, amount=amount)
            loan.save()
            messages.success(request, f'{first_name}{last_name}Your loan is: {amount} to be process')
            return redirect('loan-home')
    else:
        form = LoanCreationForm()
    return render(request, 'loan/new_loan.html', {'form': form})


class LoanCreateView(CreateView):
    model = Loan
    if(User.is_authenticated):
        fields = ['DNI', 'amount']
    else:
        fields = ['DNI', 'name', 'last_name', 'gender', 'email', 'amount']

    def form_valid(self, form):
        messages.success('Account created for!')
        return super().form_valid(form)


class LoanDetailView(DetailView):
    model = Loan
