from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signUpForm

def home(request):
    # return HttpResponse('<h1>This is Home Page!</h1>')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        
        else:
            messages.error(request, 'Invalid username or password. Please try again!')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Your account has been created successfully! You can now log in.')
            return redirect('home')
    
    else:
        form = signUpForm()
        return render(request, 'register.html', {'form': form})
