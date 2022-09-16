from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def index(request):
    return render(request, 'wallet/index.html')


def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = NewUserForm(request.POST)

        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        email = form.cleaned_data['email']
        user = authenticate(username=username, password=password, email=email)
        login(request, user)

        return redirect('index')
    else:
        #form = UserCreationForm()
        form = NewUserForm()
        return render (request=request, template_name="registration/register.html", context={'form':form})