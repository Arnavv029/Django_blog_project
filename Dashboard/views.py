from django.shortcuts import render
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def dashboard(request): 

    categories_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = { 
        'categories_count':categories_count, 
        'blogs_count':blogs_count,
    }

    return render(request, 'dashboard/dashboard.html/', context)
