from django.urls import path

from .views import (
    TaskViewSet,
    TileViewSet,
)

urlpatterns = [
    path("tiles/", TileViewSet.as_view({"get": "list"}), name="tiles"),
    path(
        "tile-info/<int:pk>",
        TileViewSet.as_view({"get": "retrieve"}),
        name="tile_details",
    ),
    path("tasks/", TaskViewSet.as_view({"get": "list"}), name="tasks"),
]
