from django.conf import settings
from django.db.models.signals import receiver
from rest_framework.authtoken.models import Token


def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
