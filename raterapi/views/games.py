from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from raterapi.models import Game
from .categories import CategorySerializer

#  todo from .game_ratings import GameRatingSerializer


class GameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    #  todo average_rating = GameRatingSerializer(many=False)

    class Meta:
        model = Game
        fields = [
            "id",
            "user_id",
            "title",
            "designer",
            "year",
            "number_of_players",
            "play_time",
            "age",
            "categories",
        ]


class GameViewSet(viewsets.ViewSet):

    def list(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True, context={"request": request})
        return Response(serializer.data)
