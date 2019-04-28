from django.db import models

class HashTag(models.Model):

  def __str__(self):
    return self.name

  name = models.CharField(max_length=50)

  objects = models.Manager()

# Create your models here.
class Article(models.Model):
  DEVELOPMENT = "DV"
  PERSONAL = "PS"
  CATEGORY_CHOICES = (
    (DEVELOPMENT, "Development"),
    (PERSONAL, "Personal")
  )

  def __str__(self):
    return self.title

  title = models.CharField(max_length=200)
  content = models.TextField()
  category = models.CharField(
    max_length=2,
    choices = CATEGORY_CHOICES,
    default= DEVELOPMENT,
  )

  hashtag = models.ManyToManyField(HashTag)

  objects = models.Manager()

# class ArticleHasHAsTag(models.Model):
#   article = models.ForeignKey(Article, on_delete=models.CASCADE)
#   hashtag = models.ForeignKey(HashTag, on_delete=models.CASCADE)


class Comment(models.Model):

  def __str__(self):
    return f"{self.username}'s comment of '{self.article}' : {self.content}"

  article = models.ForeignKey(
    Article, 
    ## Form Bring Comments Method 2 & 3
    related_name="article_comments",
    on_delete=models.CASCADE
  )
  username = models.CharField(max_length=50)
  content = models.CharField(max_length=200)
  # approved = models.BooleanField(default=False)

  objects = models.Manager()