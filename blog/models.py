from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


class Categorie(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return (self.name)


class Article(models.Model):
    title=models.CharField( max_length=50)
    desc= models.TextField()
    image= models.ImageField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    categorie= models.ForeignKey(Categorie ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
