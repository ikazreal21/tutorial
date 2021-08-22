from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from imdb import IMDb

import pyaztro


@login_required(login_url='login')
def Index(request):

    # ia = IMDb()
    horoscope = None
    if request.method == 'POST':
        search = request.POST.get('search')
        horoscope = pyaztro.Aztro(sign=search)

    #     movies = ia.search_movie(search)

    # # for director in movie['directors']:
    # #     director = director['name'])

    # # for genre in movie['genres']:
    # #     genre = genre

    context = {"horoscope": horoscope}
    return render(request, 'app1/index.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('index1')
    else:
        if request.method == 'POST':
            user = request.POST.get('username')
            passw = request.POST.get('password')
            user = authenticate(request, username=user, password=passw)

            if user is not None:
                login(request, user)
                return redirect('index1')
            else:
                messages.info(request, "Username or Password is Incorrect")

    return render(request, 'app1/login.html')


def Register(request):
    if request.user.is_authenticated:
        return redirect('index1')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account Created For " + user)
                return redirect('login')
    con = {"register": form}
    return render(request, 'app1/register.html', con)


def Logout(request):
    logout(request)
    return redirect('index1')
