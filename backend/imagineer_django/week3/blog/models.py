from django.db import models

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

  objects = models.Manager()

class Comment(models.Model):

  def __str__(self):
    return f"{self.username}'s comment of '{self.article}' : {self.content}"

  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  username = models.CharField(max_length=50)
  content = models.CharField(max_length=200)

  objects = models.Manager()

class HashTag(models.Model):

  def __str__(self):
    return self.name

  name = models.CharField(max_length=50)

  objects = models.Manager()