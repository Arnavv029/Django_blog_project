from django.shortcuts import render 
from blogs.models import Category, Blog, About
from .forms import RegistrationForm

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
    form = RegistrationForm()
    context = { 
        "form":form
    }
    return render(request, "registration.html", context)