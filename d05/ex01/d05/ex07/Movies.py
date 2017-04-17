from django.db import models
import datetime

class Movies(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    episode_nb = models.IntegerField(primary_key=True, unique=True, null=False)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    def __str__(self):
        return (self.title)
