from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message=f'Account has been created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, message=f"You have been logged in")
            return redirect('home')
        else:
            messages.error(request, message=f"Invalid Credentials! There was an error logging in, Please try again...")
            return redirect('login')
    else:
        return render(request, 'users/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('login')