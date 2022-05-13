from django.db import models


class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    album = models.TextField()
    released = models.IntegerField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
