from django.shortcuts import render, redirect
from blogs.models import Category, Blog, About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    category = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured = True)
    posts = Blog.objects.filter(is_featured=False, status=1)

    try : 
        about = About.objects.get()
    except:
        about = None 

    context = {
    "categories": category,
    "featured_post" : featured_post,
    "posts" : posts,
    "about": about,
    }
    return render(request, 'home.html', context)

def registration(request): 

    if request.method == 'POST' : 
        form = RegistrationForm(request.POST)
        if form.is_valid() : 
            form.save()
            return redirect('registration')
    else : 
        form = RegistrationForm()

    context = { 
        "form":form
    }
    return render(request, "registration.html", context)

def login(request): 

    if request.method == 'POST' :
        form = AuthenticationForm(request, request.POST)

        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None : 
                auth.login(request, user)
            return redirect('home')
        
    form = AuthenticationForm()
    context = { 
        "form":form
    }

    return render(request, "login.html", context)

def logout(request): 

    auth.logout(request)
    return redirect('home')