from rest_framework import serializers

from tasks.models import (
    Task,
    Tile,
)


class TileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        exclude = [
            "created_at",
            "updated_at",
        ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = [
            "created_at",
            "updated_at",
        ]
