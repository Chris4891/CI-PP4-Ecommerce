# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def signup_view(request):
    if request.user.is_authenticated:
        # If the user is already logged in, redirect to the home page
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # Redirect to the root URL or your desired URL
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'accAuth/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        # If user is already logged in, redirect to home
        # Replace 'home' with the name of your home view
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to the root URL
                # Assuming 'home' is the name of your root view
                return redirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'accAuth/login.html', {'form': form})
