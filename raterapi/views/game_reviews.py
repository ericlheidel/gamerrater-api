from rest_framework import viewsets, status, serializers, permissions
from django.core.exceptions import *
from rest_framework.response import Response
from raterapi.models import GameReview, Game
from django.contrib.auth.models import User


class GameReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameReview
        fields = [
            "id",
            "user_id",
            "game_id",
            "review",
        ]
        read_only_fields = ["user"]


class GameReviewViewSet(viewsets.ViewSet):
    # permission_classes = [permissions.AllowAny]

    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        reviews = GameReview.objects.all()

        serializer = GameReviewSerializer(
            reviews, many=True, context={"request": request}
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:

            review = GameReviewViewSet.objects.get(pk=pk)

            serializer = GameReviewSerializer(
                review, many=False, context={"request": request}
            )

            return Response(serializer.data)

        except GameReview.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request, pk=None):

        new_review = GameReview()

        new_review.user = request.auth.user

        new_review.game_id = request.data["game_id"]
        new_review.review = request.data["review"]

        try:

            new_review.save()

            serializer = GameReviewSerializer(new_review, context={"request": request})

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as ex:
            return Response({"error": ex.message}, status=status.HTTP_400_BAD_REQUEST)

        except PermissionDenied as ex:
            return Response({"error": ex.message}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk=None):

        try:
            user = request.auth.user

            review = GameReview.objects.get(pk=pk, game__user=user)
            review.delete()

            return Response(
                {"message": "Review removed successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )

        except GameReview.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response(
                {"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def update(self, request, pk=None):
        pass
