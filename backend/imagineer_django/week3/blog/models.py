from django.db import models

# Create your models here.
class Article(models.Model):
  DEVELOPMENT = "DV"
  PERSONAL = "PS"
  CATEGORY_CHOICES = (
    (DEVELOPMENT, "Development"),
    (PERSONAL, "Personal")
  )

  title = models.CharField(max_length=200)
  content = models.TextField()
  category = models.CharField(
    max_length=2,
    chocies = CATEGORY_CHOICES,
    default= DEVELOPMENT,
  )

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  username = models.CharField(max_length=50)
  content = models.CharField(max_length=200)

class HashTag(models.Model):
  name = models.CharField(max_length=50)