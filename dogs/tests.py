import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from dogs.models import Category, Dog


class DogTestCase(APITestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(
            name='test'
        )

        self.dog = Dog.objects.create(
            name='test',
            category=self.category
        )

    def test_get_list(self):
        """ Тест для получения списка собак """

        response = self.client.get(
            reverse('dogs:list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # print(response.json())

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "name": self.dog.name,
                        "category": self.category.name
                    }
                ]
            }
        )

    def test_dog_create(self):
        """ Тест для создания собаки """

        data = {
            'name': 'test2',
            'category': 'test'
        }

        response = self.client.post(
            reverse('dogs:dog_create'),
            dara=data
        )

        # self.assertEqual(
        #     response.status_code,
        #     status.HTTP_201_CREATED
        # )

        self.assertEqual(
            Dog.objects.all().count(),
            1
        )

    def test_dog_create_validation_error(self):
        """ Тест для проверки валидации """

        data = {
            'name': 'yest',
            'category': 'test'
        }

        response = self.client.post(
            reverse('dogs:dog_create'),
            dara=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
