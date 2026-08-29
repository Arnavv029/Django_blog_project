from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Category
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q 

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

def search(request): 

    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter( Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status=1)
    print(blogs)

    context = { 
        "blogs":blogs,
    }
    
    
    return render(request, "search.html", context)

