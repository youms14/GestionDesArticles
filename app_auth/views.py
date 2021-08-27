from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import LoginForm
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