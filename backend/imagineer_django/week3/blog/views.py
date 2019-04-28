from django.shortcuts import render
from .models import Article, Comment, HashTag

# Create your views here.
def index(request):
  category = request.GET.get('category')
  hashtag = request.GET.get('hashtag')
  
  hashtag_list = HashTag.objects.all()

  if not category and not hashtag:
    article_list = Article.objects.all()
  elif category:
    article_list = Article.objects.filter(category=category)
  else:
    article_list = Article.objects.filter(hashtag__name=hashtag)

  category_list = set([
    (article.category, article.get_category_display())
    for article in article_list
  ])

  ctx = { 
    'article_list' : article_list,
    'hashtag_list' : hashtag_list,
    'category_list': category_list
  }
  return render(request, 'index.html', ctx)

def detail(request, article_id):
  article = Article.objects.get(id=article_id)
  ## Form Bring Comments Method 1
  # comment_list = Comment.objects.filter(article__id=article_id)

  ## Form Bring Comments Method 2 
  comment_list = article.article_comments.all()
  hashtag_list = HashTag.objects.all()
  ctx = { 
    'article' : article,
    ## Form Bring Comments Method 2
    'comment_list' : comment_list,
    'hashtag_list' : hashtag_list,
  }
  return render(request, 'detail.html', ctx)

def about(request):
  pass