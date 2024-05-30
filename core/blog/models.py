from django.db import models
from blog.models import User
# Create your models here.
class Post(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length= 256)

    content =models.TextField()
    categories = models.ManyToManyField('Categories', on_delete=models.SET_NULL , null = True)
    
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



   
