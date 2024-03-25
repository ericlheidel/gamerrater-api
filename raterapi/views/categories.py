from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from raterapi.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "label"]
