from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

# User = get_user_model()

class Post(models.Model):
    
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length= 256)
    

    content =models.TextField()
    categories = models.ForeignKey('Categories', on_delete=models.SET_NULL , null = True)
    id = models.CharField(max_length=255, primary_key=True)

    status =models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    publish_date= models.DateTimeField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    

class Categories(models.Model):
    name= models.CharField(max_length=256)
    def __str__(self) :
        return self.name



   
