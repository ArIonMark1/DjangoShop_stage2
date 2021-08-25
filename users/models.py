from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='Age', default=18, blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def is_activation_key_expired(self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) < (self.activation_key_created + timedelta(hours=48)):
            return False
        return True
