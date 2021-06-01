from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=128, unique=True)
    description = models.TextField(verbose_name='Описание категории', blank=True)
