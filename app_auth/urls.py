from django.urls import path
from .views import login_blog, register
from .views import logout_blog

urlpatterns = [
    path('login',login_blog,name="login-blog"),
    path('logout',logout_blog,name="logout_blog"),
    path('register',register,name="register")
]
