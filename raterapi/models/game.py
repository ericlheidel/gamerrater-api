from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="games_created"
    )
    title = models.CharField(max_length=128, null=False)
    designer = models.CharField(max_length=128, null=False)
    year = models.IntegerField(null=False)
    number_of_players = models.IntegerField()
    play_time = models.IntegerField()
    age = models.CharField(max_length=10)
    categories = models.ManyToManyField(
        "Category", through="GameCategory", related_name="games"
    )
    # average_rating = models.ManyToManyField(
    #     "GameRate", through="GameRate", related_name="games"
    # )
