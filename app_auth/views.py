from django import forms
import django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *



def logout_blog(request):
        logout(request)
        return redirect("home")# Redirect to a success page.
    


#la fonction ci est executée quand on clique sur le formulaire
def login_blog(request):
    if request.method == "POST": #si l'utilisateur clique sur se connecter
        form = LoginForm(request.POST)
        #POST={'username':'toto', 'pwd':'password'}
        if form.is_valid():
            username= form.cleaned_data['username']
            pwd= form.cleaned_data['pwd']
            user= authenticate(username=username,password=pwd)
            if user is not None:
                login(request,user)#Cette fonction permet de stocker l'utilisateur qui s'est connecté dans l'objet request
                return redirect("home")
            else:
                messages.error(request,"! Erreur d'authentification: nom d'utilisateur ou mot de passe incorect")
                return render(request, "login2.html",{'form':form}) 
        else :
            #messages.error(request,"! Erreur d'authentification: nom d'utilisateur ou mot de passe incorect")
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'#widget permet d'attribuer des classes à des balises html
            return render(request, "login2.html",{'form':form}) 
    else:
        
        form=LoginForm()
        return render(request,"login2.html",{"form":form})
    
def register(request):
    if request.method == 'POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            pwd= form.cleaned_data['pwd']
            email=form.cleaned_data['email']
            pwd_confirm= form.cleaned_data['pwd_confirm']
            if pwd == pwd_confirm:
                user = User.objects.create_user( username=username,email=email, password=pwd)
                if user is not None:
                    return redirect('login-blog')
                else:
                    print("Erreur de création de compte")
                    msg="Erreur de création de compte"
                    #messages.error(request,"Erreur de création de compte")
                    return render(request,'register.html',{"form":form,"msg":msg})
            else:
                msg="Les mots de passe ne sont pas identiques"
                print("Les mots de passe ne sont pas identiques")
                #messages.error(request,"Les mots de passe ne sont pas identiques")
                return render(request,'register.html',{"form":form,"msg":msg})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
            return render(request, "register.html",{'form':form}) 
    else:
        form= RegisterForm()
        return render(request,'register.html',{"form":form})   
    
    
    
    
    
    
    
    
    
    """
    if request.method== "POST":
        username=request.POST["username"]
        pwd=request.POST["pwd"]
        user=authenticate(username=username,password=pwd)
        if user is not None:
           return redirect("home")
        else:
            messages.error(request,"Erreur d'authentification")
            return render(request, "login.html") 
        
        
    return render(request,"login.html")
    """