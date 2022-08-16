import re
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate,logout
from recipe.forms import UserLogin, UserRegister

# Create your views here.
def handler404(request,exception):
    return render(request,"404.html")
    
def home(request):
    return render(request,'home.html')

def registration_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            # Save the object user  
            user = form.save(commit=False)
            # hashing the password
            user.set_password(user.password)
            user.save()

            login(request,user)

            return redirect("home")
    context={
        "form":form,
    }
    return render(request,'registration.html',context)

def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("registration")

def recipes_view(request):
    return render(request, "recipes_page.html")

def recipe_detail_view(request):
    return render(request, "recipe_details.html")

def categories_view(request):
    return render(request, "categories.html")