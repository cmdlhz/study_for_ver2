from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_list(request):
  allArticles = Article.objects.all().order_by('date')
  return render(request, 'articles/article_list.html', {'articles': allArticles})

def article_detail(request, slug):
  # return HttpResponse(slug)
  AnArticle = Article.objects.get(slug=slug)
  return render(request, 'articles/article_detail.html', {'article': AnArticle })