from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
  allArticles = Article.objects.all().order_by('date')
  return render(request, 'articles/article_list.html', {'articles': allArticles})

def article_detail(request, slug):
  # return HttpResponse(slug)
  AnArticle = Article.objects.get(slug=slug)
  return render(request, 'articles/article_detail.html', {'article': AnArticle })

@login_required(login_url="/accounts/login/")
def article_create(request):
  if request.method == 'POST':
    createArticleForm = forms.CreateArticle(request.POST, request.FILES)
    if createArticleForm.is_valid():
      # Save the article to DB
      return redirect('articles:list')
  else:
    createArticleForm = forms.CreateArticle()
  return render(request, 'articles/article_create.html', { 'form': createArticleForm })