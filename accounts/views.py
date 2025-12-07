from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Registration successful! You can now log in.'
            }
            return render(request, 'success_message.html', context)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect authenticated users to home page

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Perform login logic here
            user = form.get_user()
            auth.login(request, user)
            return redirect('home')
            # return render(request, 'accounts/login_success.html')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('home')
