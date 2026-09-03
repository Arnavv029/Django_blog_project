from django.shortcuts import render,redirect
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForms,BlogPostForms,AddUserForm,EditUserForm
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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

# posts

def posts(request): 
    posts = Blog.objects.all()
    context = { 
        'posts': posts
    }
    return render(request, 'dashboard/posts.html', context )

def add_posts(request):
    if request.method == 'POST': 
        form = BlogPostForms(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False) # temporarily saving the form
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForms()
    context = { 
        'form': form
    }

    return render(request, 'dashboard/add_posts.html',context )

def edit_posts(request, pk): 
    post = get_object_or_404(Blog, pk=pk)

    if request.method == "POST": 
        form = BlogPostForms(request.POST, request.FILES, instance=post) 
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForms(instance=post)
    context = { 
        'form': form,
        'post':post
    }
    return render(request,'dashboard/edit_posts.html', context )

def delete_posts(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')

def users(request): 
    user = User.objects.all()
    context = { 
        "users":user
    }
    return render(request, 'dashboard/user.html', context)

def users_add(request):
    if request.method == "POST" : 
        form = AddUserForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = AddUserForm()
    context = { 
        'form':form
    }
    return render(request, "dashboard/users_add.html", context)

def users_edit(request, pk): 
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST": 
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid(): 
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context = { 
        "form":form,
        "user":user
    }
    return render(request, "dashboard/edit_users.html", context)

def users_delete(request, pk): 
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')