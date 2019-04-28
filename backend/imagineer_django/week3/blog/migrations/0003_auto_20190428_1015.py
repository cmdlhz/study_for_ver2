# Generated by Django 2.2 on 2019-04-28 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='blog.Article'),
        ),
    ]