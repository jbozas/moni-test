from django.shortcuts import render, redirect
from .models import Loan
from users.models import Profile
from .verification import ItsApproved
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoanCreationForm, LoanAlternCreationForm
from django.views.generic import (CreateView,
                                  DetailView)


def home(request):
    return render(request, 'loan/home.html')


def about(request):
    return render(request, 'loan/about.html')


def NewLoan(request):
    form = GetForm(request)
    if request.method == 'POST':
        if form.is_valid():
            # Ask if the user has active session
            loan = GetLoan(request, form)
            loan.save()
            # Give the message
            if(loan.approved):
                messages.success(request, f"Dear {loan.first_name} {loan.last_name}, your cash advance of ${loan.amount} has been approved")
            else:
                messages.warning(request, f"Dear {loan.first_name} {loan.last_name}, your cash advance of ${loan.amount} hasn't been approved")
                # return redirect('loan-home')
    else:
        if(request.user.is_authenticated):
            form = LoanAlternCreationForm()
        else:
            form = LoanCreationForm()
    return render(request, 'loan/new_loan.html', {'form': form})

def GetLoan(request, form):
    if(request.user.is_authenticated):
        profile = Profile.objects.get(user=request.user)
        return Loan(document=profile.document, first_name=profile.first_name, last_name=profile.last_name, email=profile.email, gender=profile.gender, approved=ItsApproved(profile.document), amount=form.cleaned_data.get('amount'))
    return Loan(document=form.cleaned_data.get('document'), first_name=form.cleaned_data.get('first_name'), last_name=form.cleaned_data.get('last_name'), email=form.cleaned_data.get('email'), gender=form.cleaned_data.get('gender'), approved=ItsApproved(form.cleaned_data.get('document')), amount=form.cleaned_data.get('amount'))

def GetForm(request):
    if(request.user.is_authenticated):
        return LoanAlternCreationForm(request.POST)
    return LoanCreationForm(request.POST)

class LoanCreateView(CreateView):
    model=Loan
    if(User.is_authenticated):
        fields=['DNI', 'amount']
    else:
        fields=['DNI', 'name', 'last_name', 'gender', 'email', 'amount']

    def form_valid(self, form):
        messages.success('Account created for!')
        return super().form_valid(form)


class LoanDetailView(DetailView):
    model=Loan
