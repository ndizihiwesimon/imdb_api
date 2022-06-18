from urllib import response
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "username": "testcase",
            "email": "testcase@example.com",
            "password": "NewPassword@123",
            "password2": "NewPassword@123"
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 


class LoginLogoutTestCase(APITestCase):

    def setup(self):
        self.user = User.objects.create_user(username="Nomiso", password="Hello@123")

    def test_login(self):
        data = {
            "username": "Nomiso",
            "password": "Hello@123",
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)