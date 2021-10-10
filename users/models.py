from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    image = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='Age', default=18, blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def is_activation_key_expired(self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) < (self.activation_key_created + timedelta(hours=48)):
            return False
        return True


class ProfileUser(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    CRAZY_PEOPLE = 'MP'

    GENDER_CHOICE = (
        (None, 'Выберите ваш пол'),
        (MALE, 'мужчина'),
        (FEMALE, 'женщина'),
        (CRAZY_PEOPLE, 'разнополый_гуманоид'),
    )

    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICE, blank=True, null=True, default=None, max_length=1, verbose_name='пол')
    tagline = models.CharField(max_length=128, blank=True, verbose_name='теги')
    description = models.TextField(blank=True, max_length=256, verbose_name='о себе')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profileuser.save()
