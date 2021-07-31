from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICES = [("1", "live"), ("2", "pending"), ("3", "archived")]

TYPE_CHOICES = [("1", "survey"), ("2", "discussion"), ("3", "diary")]


class Tile(models.Model):
    launch_date = models.DateField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        def __str__(self):
            return self.launch_date


class Task(models.Model):

    title = models.CharField(max_length=50, blank=True)
    order = models.CharField(max_length=50, blank=True)
    description = models.TextField(
        blank=True, null=True, help_text="Description of the task"
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=50, blank=True)

    tile = models.ForeignKey(Tile, blank=True, null=True, on_delete=models.PROTECT)

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        def __str__(self):
            return self.title
