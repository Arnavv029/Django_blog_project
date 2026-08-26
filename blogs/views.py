from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Category
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.

def post_by_category(request,pk): 
    post = Blog.objects.filter(status=1, category=pk)

    try : 
         category = Category.objects.get(id=pk)
    except : 
        return redirect('home')
    
    context = { 
        'posts': post,
        'category': category
    }
    return render(request, 'post_by_category.html', context )

def blogs(request, slug):

    single_blog = get_object_or_404(Blog, slug=slug, status=1)

    constext = { 
        "single_blog" : single_blog
    }

    return render(request, "blogs.html", constext)

