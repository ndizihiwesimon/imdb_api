from turtle import st
from urllib import response
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist.api import serializers
from watchlist import models

class StreamPlatformTestCase(APITestCase):
    """Defining test methods for my stream platform."""
    
    def setUp(self):
        self.user = User.objects.create_user(username='nomiso', password='Password@123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Nomiso", 
                                    about="#1 Streaming Platform", website="https://www.nomiso.net")

    def test_stream_platform_create(self):
        data = {
            "name": "Nomiso",
            "about": "#1 Streaming platform",
            "website": "https://nomiso.com"
        }
        response = self.client.post(reverse('stream-platform-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_stream_platform_list(self):
        response = self.client.get(reverse('stream-platform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stream_platform_ind(self):
        response = self.client.get(reverse('stream-platform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_stream_platform_update(self):
    #     data = {
    #         "name": "Siga Inkweto",
    #         "about": "#2 Streaming platform",
    #         "website": "https://siga.com"
    #     }
    #     response = self.client.put(reverse('stream-platform-update', args=(self.stream.id,), data=data))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_stream_platform_del(self):
    #     response = self.client.delete(reverse('stream-platform-delete', args=(self.stream.id,)))
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class WatchListTestCase(APITestCase):
  
    def setUp(self):
        self.user = User.objects.create_user(username='nomiso', password='Password@123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Nomiso",
                                                           about="#1 Streaming Platform", website="https://www.nomiso.net")

        self.watchList = models.WatchList.objects.create(platform=self.stream, title="Adam Project",
                                                           storyline="Example Movie", active = True)



    def test_watchList_create(self):

        data = {
            "platform": self.stream,
            "title": "Test movie",
            "storyline": "Example story",
            "active": True,
        }
        response = self.client.post(reverse('watch-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchList_list(self):
        response = self.client.get(reverse('watch-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchList_ind(self):
        response = self.client.get(reverse('watchList-detail', args=(self.watchList.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, "Adam Project")

class ReviewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='nomiso', password='Password@123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Nomiso",
                                                           about="#1 Streaming Platform", website="https://www.nomiso.net")

        self.watchList = models.WatchList.objects.create(platform=self.stream, title="Adam Project",
                                                           storyline="Example Movie", active = True)

    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Amazing",
            "watchlist": self.watchList,
            "active": True
        }
        response = self.client.post(reverse('review-create', args=(self.watchList.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            reverse('review-create', args=(self.watchList.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    # def test_review_create(self):