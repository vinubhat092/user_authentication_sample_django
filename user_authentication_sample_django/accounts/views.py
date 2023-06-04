from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from accounts.forms import emailregistration
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
def home(request):
    return render(request,"index.html",{})


def register(request):
    form = emailregistration(request.POST or None)
    print("fsfaakj",form)
    if form.is_valid():
        email = form.cleaned_data['email']
        # password = form.cleaned_data['password']
        User.objects.create_user(username=email,email=email)
        return redirect('/login')
    form = {
        "form":form
    }
    return render(request,"register.html",form)

def login_view(request):
    print("jkshf")
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        print("djd",form)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=email,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
        else:
            AuthenticationForm(request)
        context = {
            "form":form
        }
        return render(request,"login.html",context)
    return render(request,"login.html",{})

def logout_view(request):
    if request.method == "POST":
        # print("comings")
        logout(request)
        return redirect("/login/")
    return render(request,"logout.html",{})