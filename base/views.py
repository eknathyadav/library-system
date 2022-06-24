import email
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from .models import User
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    print(request.user)
    return render(request, 'base/index.html')


def loginUser(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base:main')
        else:
            # No backend authenticated the credentials
            messages.add_message(request, messages.INFO,
                                 'Invalid Email or Password. Please enter the right credentials')
    context = {'page': page}
    return render(request, 'base/login-register.html', context)


def registerUser(request):
    page = 'register'
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        name = request.POST['fullname'].split()
        firstname = name[0]
        lastname = name[1]
        try:
            user = User.objects.create_user(
                email=username,
                password=password,
                first_name=firstname,
                last_name=lastname
            )
            user.save()
            return redirect('base:main')
        except:
            messages.add_message(request, messages.INFO,
                                 'Email is already in use')

    context = {'page': page}
    return render(request, 'base/login-register.html', context)


# redirect when user is not logged in
@login_required(login_url='base:login-user')
def main(request):
    return render(request, 'base/main.html')


@login_required(login_url='base:login-user')
def addBook(request):
    context = {'page': 'add'}
    return render(request, 'base/add-book.html', context)


@login_required(login_url='base:login-user')
def showBook(request, pk):
    context = {
        'pk': pk
    }
    return render(request, 'base/book.html', context)


@login_required(login_url='base:login-user')
def updateBook(request, pk):
    context = {
        'pk': pk,
        'page': 'update'
    }
    return render(request, 'base/update-book.html', context)


def logoutUser(request):
    logout(request)
    return redirect('base:home')
