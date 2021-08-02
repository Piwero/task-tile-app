from rest_framework import viewsets

from tasks.models import (
    Task,
    Tile,
)

from .serializers import (
    TaskSerializer,
    TileSerializer,
)


class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
