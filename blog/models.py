from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse


class Categorie(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return (self.name)


class Article(models.Model):
    title=models.CharField( max_length=50)
    desc= models.TextField()
    image= models.ImageField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)#auto_now=True
    categorie= models.ForeignKey(Categorie ,on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
    def is_valid_date(self):
        return self.created_at <= self.updated_at
         

#Article.objects.all()
