from collections import UserString
from socket import fromshare
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import Group
from hawkerapp.decorators import unauthenticated_user
from .models import Location, Food, Stall, Review
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, customer_only, hawker_only


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# Create your views here.


@unauthenticated_user
def registercustomer(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            messages.success(request, "Account was created for " + username)
            return redirect('login')
    context = {"form":form}
    return render(request, "hawkerapp/registercustomer.html", context)

@unauthenticated_user
def registerhawker(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name="hawker")
            user.groups.add(group)
            messages.success(request, "Account was created for " + username)
            return redirect('login')
    context = {"form":form}
    return render(request, "hawkerapp/registerhawker.html", context)

@unauthenticated_user
def loginPage(request):
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
@customer_only
def index(request):
    locations = Location.objects.all().order_by('rating')
    reviews = Review.objects.all().order_by("-id")
    return render(request, "hawkerapp/index.html", {"locations":locations, "reviews":reviews})


@login_required(login_url="login")
@hawker_only
def stallprofilehawker(request, stall_id): 
    stall = Stall.objects.get(id=stall_id)
    reviews = stall.reviews.all()
    mean_rating = 0
    reviews_count = 0
    for review in reviews:
        mean_rating += review.rating
        reviews_count += 1
    if reviews_count > 0:
        mean_rating = mean_rating/reviews_count
    else:
        mean_rating = 0
    return render(request, "hawkerapp/stallprofilehawker.html", {"stall":stall, "menu":stall.foods.all(), "reviews": reviews, "mean_rating":round(mean_rating,1), "reviews_count":reviews_count})
    
@login_required(login_url="login")
@hawker_only
def hawkerprofile(request):
    stalls = Stall.objects.filter(owner=request.user)
    return render(request, "hawkerapp/hawkerprofile.html", {"stalls":stalls})

@login_required(login_url="login")
@customer_only
def customerprofile(request):
    reviews = Review.objects.filter(owner=request.user)
    return render(request, "hawkerapp/customerprofile.html", {"reviews":reviews})


@login_required(login_url="login")
@customer_only
def stallprofilecustomer(request, stall_id): 
    stall = Stall.objects.get(id=stall_id)
    reviews = stall.reviews.all()
    mean_rating = 0
    has_rating = False
    for review in reviews:
        mean_rating += review.rating
        has_rating = True
    if has_rating:
        mean_rating = mean_rating/reviews.count()
    else:
        mean_rating = 0
    return render(request, "hawkerapp/stallprofilecustomer.html", {"stall":stall, "menu":stall.foods.all(), "reviews":reviews, "mean_rating":round(mean_rating,1), "reviews_count":reviews.count()})

@login_required(login_url="login")
@customer_only
def addreview(request, stall_id):
    stall = Stall.objects.get(id=stall_id)
    if request.method =="POST":
        description = request.POST["description"]
        rating = request.POST["rating"]
        image = request.FILES["image"]
        review = Review(stall=stall, owner=request.user, description=description, rating=int(rating), image=image)
        review.save()
        reviews = stall.reviews.all()
        return render(request, "hawkerapp/stallprofilecustomer.html", {"stall":stall, "menu":stall.foods.all(), "reviews":reviews})
    return render(request, "hawkerapp/addreview.html", {"stall":stall})

@login_required(login_url="login")
@hawker_only
def addstall(request):
    if request.method == "POST":
        owner = str(request.user)
        location = Location.objects.get(id=request.POST["location"])
        stall_name = request.POST["stallname"]
        stall = Stall(owner=owner, name=stall_name, location=location)
        stall.save()
        for id in request.POST.getlist("food"):
            food = Food.objects.get(id=id)
            stall.foods.add(food)
        return render(request, "hawkerapp/stallprofilehawker.html", {"stall":stall, "menu":stall.foods.all()})
    location = Location.objects.all()
    food = Food.objects.all()
    return render(request, "hawkerapp/addstall.html", {"location":location, "food":food})


@login_required(login_url="login")
@customer_only
def resultspagebysearchbar(request):
    results = []
    if request.method == "POST":
        if request.POST["searchby"] == "hawkercentre":
            loc = request.POST["search"]
            location_list = Location.objects.filter(name__icontains = loc)
            num_stores = 0
            for location in location_list:
                stalls = Stall.objects.filter(location=location)
                results.append(stalls)
                num_stores += stalls.count()
            if num_stores == 0:
                results = None
            return render(request, "hawkerapp/resultspagebysearchbar.html", {"results":results})
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
            return render(request, "hawkerapp/resultspagebysearchbar.html", {"results": results})


@login_required(login_url="login")
@customer_only
def location(request,location_name):
    location = Location.objects.get(name=location_name)
    return render(request, "hawkerapp/location.html", {"location":location})