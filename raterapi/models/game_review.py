from django.db import models
from django.contrib.auth.models import User


class GameReview(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews_created"
    )
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="games")
    review = models.TextField()
