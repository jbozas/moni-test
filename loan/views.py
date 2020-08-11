from django.shortcuts import render
from django.views.generic import (CreateView,
    DetailView)
from .models import Loan


def home(request):
    return render(request, 'loan/home.html')


def about(request):
    return render(request, 'loan/about.html')


class LoanCreateView(CreateView):
    model = Loan
    fields = ['DNI', 'name', 'last_name', 'gender', 'email', 'amount']

    def form_valid(self, form):
        return super().form_valid(form)

class LoanDetailView(DetailView):
    model = Loan
