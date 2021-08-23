from blog.models import Article

def run():
    for i in range(12,20):
        article=Article()
        article.title= "Article N° #%d "% i
        article.desc="Description de l'article N° #%d "% i
        article.image = "http://default"
        article.save()
print("operation réussie")