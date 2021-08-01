import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from tasks.models import (
    Task,
    Tile,
)


class TileTests(TestCase):
    def setUp(self):
        self.tile1 = Tile.objects.create(
            launch_date=datetime.datetime.now(), status="live"
        )
        self.tile2 = Tile.objects.create(
            launch_date=datetime.datetime.now(), status="pending"
        )

    def test_tiles_url(self):
        response = self.client.get(reverse("tiles"))
        self.assertEqual(response.status_code, 200)

    def test_api_get_tiles(self):
        response_tile_list = self.client.get(reverse("tiles"))
        json_tile_list = response_tile_list.json()
        self.assertEqual(len(json_tile_list), 2)
        self.assertEqual(f"{self.tile1.status}", "live")

    def test_tile_details_url(self):
        response = self.client.get(reverse("tile_details", args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_api_retrieve_tile_details(self):
        response_tile_details = self.client.get(reverse("tile_details", args=[1]))
        json_tile_details = response_tile_details.json()
        self.assertEqual(json_tile_details["status"], "live")


class TasksTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="usertest", password="foo")
        tile1 = Tile.objects.create(launch_date=datetime.datetime.now(), status="live")
        tile2 = Tile.objects.create(
            launch_date=datetime.datetime.now(), status="pending"
        )
        self.task1 = Task.objects.create(
            title="task1",
            order="order1",
            description="desc1",
            type="survey",
            user=user,
            tile=tile1,
        )
        self.task2 = Task.objects.create(
            title="task2",
            order="order2",
            description="desc2",
            type="discussion",
            user=user,
            tile=tile2,
        )

    def test_tasks_url(self):
        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 200)

    def test_api_get_tasks(self):
        response_tasks_list = self.client.get(reverse("tasks"))
        json_tasks_list = response_tasks_list.json()
        self.assertEqual(len(json_tasks_list), 2)
        self.assertEqual(f"{self.task1.title}", "task1")
        self.assertEqual(json_tasks_list[0]["tile"], 1)
