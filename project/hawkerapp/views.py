from socket import fromshare
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import HawkerOwner, Location, Food, Stall
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# Create your views here.



def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect('login')
        context = {"form":form}
        return render(request, "hawkerapp/register.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.info(request, "Username OR Password Is Incorrect")
        context = {}
        return render(request, "hawkerapp/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def index(request):
    results = []
    if request.method == "POST":
        if request.POST["searchby"] == "hawkercentre":
            loc = request.POST["search"]
            location_list = Location.objects.filter(name__icontains = loc)
            num_stores = 0
            for location in location_list:
                stalls = (Stall.objects.filter(location=location))
                results.append(stalls)
                num_stores = stalls.count()
            if num_stores == 0:
                results = None
            return render(request, "hawkerapp/index.html", {"results":results})
        else:
            food = request.POST["search"]
            food_list = Food.objects.filter(name__icontains = food)
            repeat = []
            num_stores = 0
            for food in food_list:
                to_add = []
                stalls = Stall.objects.filter(foods=food)
                for stall in stalls:
                    if stall.id not in repeat:
                        to_add.append(stall.id)
                        num_stores += 1
                results.append(Stall.objects.filter(pk__in=to_add))
                repeat += to_add
            if num_stores == 0:
                results = None
            return render(request, "hawkerapp/index.html", {"results": results})

    return render(request, "hawkerapp/index.html", {"results":results})


@login_required(login_url="login")
def profile(request, stall_id): 
    stall = Stall.objects.get(id=stall_id)
    return render(request, "hawkerapp/profile.html", {"stall":stall, "menu":stall.foods.all()})

