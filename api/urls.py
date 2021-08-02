from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from .views import (
    TaskViewSet,
    TileViewSet,
)

urlpatterns = [
    path("tiles/", TileViewSet.as_view({"get": "list"}), name="tiles"),
    path(
        "tile-info/<int:pk>",
        TileViewSet.as_view(
            {"get": "retrieve", "put": "update", "post": "create", "delete": "destroy"}
        ),
        name="tile_details",
    ),
    path("tasks/", TaskViewSet.as_view({"get": "list"}), name="tasks"),
    path(
        "task-info/<int:pk>",
        TaskViewSet.as_view(
            {
                "get": "retrieve",
                "post": "create",
                "put": "update",
                "post": "create",
                "delete": "destroy",
            }
        ),
        name="task_details",
    ),
]

urlpatterns += [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
