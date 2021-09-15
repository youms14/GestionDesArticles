from blog.models import Article
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from app_auth.forms import  ArticleForm

# Create your views here.

@login_required
def dashboard(request):
    return render(request,'db.html')

@login_required #décoration ou annotation 
def user_articles(request):
    """if not request.user.is_authenticated:
        return redirect('login-blog') #ou  @login_required"""
    
    has_perm=False
    if request.user.has_perm("blog.delete_article"):
        has_perm=True
    list_articles = Article.objects.filter(user=request.user)
    return render(request, 'my-articles.html', {'list_article':list_articles,"has_perm":has_perm})


class AddArticle(LoginRequiredMixin,CreateView):
    model= Article
    form_class = ArticleForm
    template_name = "add-article.html"
    success_url = "my-articles"
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class UpdateArticle(LoginRequiredMixin ,UpdateView):
    model=Article
    form_class = ArticleForm
    template_name ='app_admin/article_form.html'
    success_url="/app-admin/my-articles"
    
class DeleteArticle(DeleteView):
    model= Article
    success_url = "/app-admin/my-articles"
    """"Cette foonction permet d'interdire à un utilisateur d'effectuer une tâche(comme delete)"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('blog.delete_article'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
     