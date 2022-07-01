from ast import For
from os import stat
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

    # FORBIDDEN because they DO NOT have admin permissions
    def test_stream_platform_update(self):
        data = {
            "name": "Siga Inkweto",
            "about": "#2 Streaming platform",
            "website": "https://siga.com"
        }
        response = self.client.put(reverse('stream-platform-detail', args=(self.stream.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # FORBIDDEN because they DO NOT have admin permissions
    def test_stream_platform_del(self):
        response = self.client.delete(reverse('stream-platform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


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
        self.watchList2 = models.WatchList.objects.create(platform=self.stream, title="Adam Project",
                                                         storyline="Example Movie", active=True)
        self.review = models.Review.objects.create(review_user=self.user, rating = 5, description = "Great movie",
                                                         watchlist=self.watchList2, active=True)

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
        self.assertEqual(models.Review.objects.count(), 2)
        # self.assertEqual(models.Review.objects.get().rating, 5)

        response = self.client.post(
            reverse('review-create', args=(self.watchList.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_review_create_unauth(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Great movie",
            "watchlist": self.watchList,
            "active": True
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(
            reverse('review-create', args=(self.watchList.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            "review_user": self.user,
            "rating": 4,
            "description": "Great movie - Updated",
            "watchlist": self.watchList,
            "active": False
        }
        response = self.client.put(reverse('review-details', args=(self.review.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchList.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # Commented out to avoid 429 STATUS CODE too many requests
    # def test_review_ind(self):
    #     response = self.client.get(reverse('review-details', args=(self.review.id,)))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_delete(self):
        response = self.client.delete(reverse('review-details', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_review_user(self):
        response = self.client.get('/watch/user-review/?username='+ self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)