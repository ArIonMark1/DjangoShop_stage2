from django.db import models
from django.forms import ModelForm


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=128, unique=True)
    description = models.TextField(verbose_name='Описание категории', blank=True)
    is_active = models.BooleanField(verbose_name='active', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='active', default=True)

    def __str__(self):
        return f'{self.name} | {self.category}'


# class ProductAdminForm(ModelForm):
#
#     class Meta:
#         model = Product
#         fields = ('name', 'description', 'image', 'price', 'quantity', 'category', 'is_active',)
