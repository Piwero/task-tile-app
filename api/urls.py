from django.urls import path

from .views import (
    TaskViewSet,
    TileViewSet,
)

urlpatterns = [
    path("tiles/", TileViewSet.as_view({"get": "list"}), name="tiles"),
    path("tasks/", TaskViewSet.as_view({"get": "list"}), name="tasks"),
]
