from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import NewUserForm

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
        #form = UserCreationForm()
        form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={'form':form})