from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Category
from django.shortcuts import redirect

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

