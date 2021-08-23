from django.contrib import admin

from .models import Article, Categorie

admin.site.register(Article)#ajout de du modèle Article
admin.site.register(Categorie)