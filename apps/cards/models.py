from django.db import models
from apps.decks.models import Decks


class Card(models.Model):
    deck = models.ForeignKey(Decks, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    buckets = (
        (1, '1 Day'),
        (2, '3 Days'),
        (3, '7 Days'),
        (4, '16 Days'),
        (5, '30 Days')
    )
    bucket = models.IntegerField(choices=buckets, default=1)
    next_review_at = models.DateField()
    last_reviewed_at = models.DateTimeField()
