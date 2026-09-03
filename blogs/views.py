from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Category, Comment
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
    if request.method == "POST" : 
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save() 
        return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    
    constext = { 
        "single_blog" : single_blog,
        "comments":comments,
        "comment_count":comment_count
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

