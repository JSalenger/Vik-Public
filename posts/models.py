from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.template.defaultfilters import slugify
User = get_user_model()
# Create your models here.'
class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    likes = models.ManyToManyField(get_user_model(), blank=True, related_name="article_likes")
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    class Meta:
        ordering = ('-date',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])\


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
