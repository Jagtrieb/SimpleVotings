from django.contrib.auth.models import User
from django.db import models


class Vote(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    mode = models.IntegerField(default=0)

class Option(models.Model):
    name = models.CharField(max_length=64)
    count = models.IntegerField(default=0)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)