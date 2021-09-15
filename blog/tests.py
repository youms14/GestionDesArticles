from datetime import date
from django.test import TestCase
from datetime import datetime,date
from .models import is_valid_date, Article,Categorie

class ArticleTestCase(TestCase):
    
    def setUp(self):
        
        #Create Categorie
        c1= Categorie.objects.create(name="Ordinateurs")
        #Create Articles
        a1= Article.objects.create(title="Lenovo Rizen 4", desc="PC utilisable pour jeux et vidéos",categorie=c1, created_at=date(2016, 10, 7), updated_at=datetime.now())
        a2= Article.objects.create(title="Dell Precision", desc="PC utilisable pour jeux et vidéos",categorie=c1, created_at=datetime.now(), updated_at=date(2016, 10, 7))
        
    def test_is_valid_date(self):
        a= Article.objects.get(id=109)
        self.assertTrue(a.is_valid_date())
        
        
