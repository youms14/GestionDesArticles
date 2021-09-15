from django.http import request
from django.shortcuts import render

from blog.models import Article, Categorie

# view c'est où on écrit la logique
#request=requete http
def home (request):
    liste_articles=Article.objects.all().order_by("-created_at")
    print(liste_articles)
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

def search (request):
    query=request.GET["article"]# GET={"article":"voiture"}: GET est un dictionnaire dont les clés sont les names des formulaires et les valeurs sont les saisies.  
    liste_articles=Article.objects.filter(title__icontains=query)
    return render(request,"search.html",{"list":liste_articles,"query":query})