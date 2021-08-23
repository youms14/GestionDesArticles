from django.http import request
from django.shortcuts import render

from blog.models import Article, Categorie

# view c'est où on écrit la logique
#request=requete http
def home (request):
    liste_articles=Article.objects.all()
    return render(request,"index.html", { "list":liste_articles})

def details(request, id):
    article= Article.objects.get(pk=id)
    categorie=article.categorie
    others= Article.objects.filter(categorie=categorie)
    context={
        "article": article,
        "others": others
    }
    return render(request,"details.html",context)