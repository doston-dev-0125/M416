from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import BookForm, SignUpForm
from .models import MyUser,Book
from django.views.generic import CreateView


def home(request):
    return render(request,'index.html')

def specifications(request):
    return render(request,'cs.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)
    

def order(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    
    }

    return render(request, 'book.html', context)



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username yoki password xato!')
            return redirect('login')

    return render(request, 'login.html')
    

