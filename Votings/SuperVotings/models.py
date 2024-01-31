from django.contrib.auth.models import User
from django.db import models


class Vote(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    mode = models.IntegerField(default=0)
class Participant(models.Model):
    name = models.CharField(max_length=64)
    vote_id = models.IntegerField(default=0)
    count = models.IntegerField(default=0)