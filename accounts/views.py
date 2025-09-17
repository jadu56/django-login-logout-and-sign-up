from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def home(request):
    return render(request, "home.html")

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "profile.html")


# Create your views here.
