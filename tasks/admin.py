from django.contrib import admin

from .models import (
    Task,
    Tile,
)


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    model = Tile
    list_display = ["id", "launch_date", "status"]
    list_filter = ["launch_date", "status"]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = [
        "title",
        "order",
        "description",
        "tile",
        "type",
        "user",
    ]
    list_filter = ["order", "type", "tile", "user"]
    readonly_fields = ["created_at", "updated_at"]
