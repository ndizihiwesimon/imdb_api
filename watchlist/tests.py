from cgitb import reset
import imp
from os import stat
from urllib import response
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist.api import serializers
from watchlist import models

class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='nomiso', password='Password@123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)

    def test_stream_platform_create(self):
        data = {
            "name": "Netflix",
            "about": "#1 Streaming platform",
            "website": "https://netflix.com"
        }
        response = self.client.post(reverse('stream-platform-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)