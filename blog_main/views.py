from django.shortcuts import render 
from blogs.models import Category, Blog 

def home(request):
    category = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured = True)
    posts = Blog.objects.filter(is_featured=False, status=1)

    context = {
    "categories": category,
    "featured_post" : featured_post,
    "posts" : posts,
    }
    return render(request, 'home.html', context)