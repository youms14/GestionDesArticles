from django import forms
from django.forms import widgets
from django.forms.models import ModelForm
from django.views.generic.edit import UpdateView
from blog.models import Article

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    pwd_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
class ArticleForm (forms.ModelForm):
    class Meta:
        model= Article
        fields= ['title','categorie','desc','image']
        labels= {'title':'Titre','categorie': 'Categorie','desc':'Description','image':'Image',     'title':'Titre','categorie': 'Categorie','desc':'Description','image':'Image'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class':'form-control','rows':5}),
            #'image':forms.ImageField()
        }

