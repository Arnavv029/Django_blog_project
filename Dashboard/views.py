from django.shortcuts import render,redirect
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForms
from django.shortcuts import get_object_or_404

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

def categories(request) : 
    return render(request, 'dashboard/categories.html/' )

def add_categories(request): 

    if request.method == 'POST' :
        form = CategoryForms(request.POST)
        if form.is_valid() : 
            form.save()
            return redirect('categories')

    form = CategoryForms() 
    context = { 
        "form":form
    }

    return render(request, 'dashboard/add_categories.html',context )

def edit_categories(request, pk): 
    categories = get_object_or_404(Category, pk=pk)
    if request.method == "POST": 
        form = CategoryForms(request.POST, instance=categories)
        if form.is_valid(): 
            form.save()
            return redirect('categories')
    form = CategoryForms(instance=categories)
    context = { 
        'form':form
    }
    return render(request, 'dashboard/edit_categories.html', context )

def delete_categories(request, pk): 
    categories = get_object_or_404(Category, pk=pk)
    categories.delete()
    return redirect('categories')