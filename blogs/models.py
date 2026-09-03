from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model): 

    category_name = models.CharField(unique=True)
    created_by = models.DateTimeField(auto_now_add=True)
    update_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
    
STATUS_CHOICES=( 
    (0, "Draft"),
    (1, "Published")
)
    
class Blog(models.Model) :

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to="uploads/%y/%m/%d")
    short_description= models.TextField(max_length=500)
    blog_body=models.TextField(max_length=2000)
    status=models.IntegerField(choices=STATUS_CHOICES, default=0)
    is_featured=models.BooleanField(default=False)
    created_by = models.DateTimeField(auto_now_add=True)
    update_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class About(models.Model) : 

    about_heading = models.CharField(max_length=30)
    about_descrition = models.TextField(max_length=255)

    def __set__(self):
        return self.about_heading

class SocialLink(models.Model): 
    platform = models.CharField(max_length=25)
    link = models.URLField(max_length=100)
    created_by = models.DateTimeField(auto_now_add=True)
    update_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
