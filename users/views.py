from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            save_profile(form, username)
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def save_profile(form, username):
    profile = Profile(user=User.objects.get(username=username), document=form.cleaned_data.get('document'), first_name=form.cleaned_data.get('first_name'), last_name=form.cleaned_data.get('last_name'), email=form.cleaned_data.get('email'), gender=form.cleaned_data.get('gender'))
    profile.save()
