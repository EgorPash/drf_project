from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from customs.models import Customs
from users.models import User


class CustomsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="django@mail.ru", password='DXB')
        self.custom = Customs.objects.create(
            owner=self.user, place="Home", time="12:00:00", action="Зарядка", duration='40'
        )
        self.client.force_authenticate(user=self.user)

    def test_customs_retrieve(self):
        url = reverse("customs:customs_retrieve", args=(self.custom.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.custom.place)

    def test_customs_create(self):
        url = reverse("customs:customs_create")
        data = {
            "owner": self.user.pk,
            "place": "Home",
            "time": "12:00",
            "action": "Зарядка",
            "duration": "40",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customs.objects.all().count(), 2)

    def test_customs_update(self):
        url = reverse("customs:custom_update", args=(self.custom.pk,))
        data = {
            "place": "Work",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customs.objects.get(pk=self.custom.pk).place, "Work")

    def test_customs_delete(self):
        url = reverse("customs:customs_delete", args=(self.custom.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customs.objects.all().count(), 0)

    def test_customs_list(self):
        url = reverse(
            "customs:customs_list",
        )
        response = self.client.get(url)
        data = response.status_code
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
