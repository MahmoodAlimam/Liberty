from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You are at the wallet index.")


def index(request):
    return render(request, 'wallet/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'registration/register.html', context)