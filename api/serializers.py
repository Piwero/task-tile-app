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
    tile_status = serializers.SerializerMethodField()
    launch_date = serializers.SerializerMethodField()
    assigned_to = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "title",
            "order",
            "description",
            "type",
            "tile_status",
            "launch_date",
            "assigned_to",
        ]

    def get_tile_status(self, obj):
        tile_status = obj.tile.status
        return tile_status

    def get_launch_date(self, obj):
        tile_launch_date = obj.tile.launch_date
        return tile_launch_date

    def get_assigned_to(self, obj):
        user_task_assigned = obj.user.username
        return user_task_assigned
