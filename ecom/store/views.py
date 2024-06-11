from django.shortcuts import render, redirect
from .models import Category, Product, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def category(request, foo):  # Foo is the name of the category
    # Edits out the hyphen needed in URLs and swaps in a space
    foo = foo.replace('-', ' ')
    # Get the category from the URL
    try:
        # Look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, "category.html", {"products": products, "category": category})

    except:
        messages.success(request, "That category does not exist. Please try again!")
        return redirect("home")


def product(request, pk):
    product = Product.objects.get(id=pk)  # PK is primary key and is a product key number
    return render(request, "product.html", {"product": product})


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def about(request):
    return render(request, "about.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect("home")
        else:
            messages.info(request, "Username or password is incorrect. Please try again!")
            return redirect("login")
    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out! Thanks for visiting!"))
    return redirect("home")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            # Log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been registered! You are now logged in!"))
            return redirect("home")
        else:
            messages.success(request, ("There was a problem! Please try again."))
            return redirect("register")

    return render(request, "register.html", {"form": form})
