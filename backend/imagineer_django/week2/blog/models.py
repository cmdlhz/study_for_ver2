from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=30)
  contents = models.TextField()
  view_count = models.IntegerField()

  def __str__(self):
    return self.title

  objects = models.Manager()

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  comment = models.CharField(max_length=100)

  objects = models.Manager()          