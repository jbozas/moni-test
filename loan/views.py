from django.shortcuts import render
from django.views.generic import (CreateView,
                                  DetailView)
from .models import Loan
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request, 'loan/home.html')


def about(request):
    return render(request, 'loan/about.html')


def newLoan(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class LoanCreateView(CreateView):
    model = Loan
    if(User.is_authenticated):
        print(f"USUARIO {User.last_name}")
        fields = ['DNI', 'amount']
    else:
        fields = ['DNI', 'name', 'last_name', 'gender', 'email', 'amount']

    def form_valid(self, form):
        messages.success('Account created for!')
        return super().form_valid(form)


class LoanDetailView(DetailView):
    model = Loan
