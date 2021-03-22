from django.db import models


class Decks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_reviewed = models.DateTimeField()
