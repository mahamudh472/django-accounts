from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('admin:index')  # Redirect to the admin index or any desired page
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("Login successful")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', context={'form': form})