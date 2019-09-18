#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model
class Poll(models.Model):
    question = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    class Meta:
        ordering = ('-date',)
    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(
        'Poll',
        on_delete=models.CASCADE,
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Voter(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
