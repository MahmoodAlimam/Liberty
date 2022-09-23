from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'wallet/index.html')


def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
        # dob = form.cleaned_data['DOB']
            email = form.cleaned_data['email']
        #raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password, email=email)
            login(request, user)

        return redirect('index')
    else:
        form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={'form':form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form":form})