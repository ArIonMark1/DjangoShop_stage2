from django.db import models

from mainapp.models import Product
from users.models import User


# Create your models here.

# второй способ переопределения
class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.products.quantity += object.quantity
            object.products.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()  # вызываем для управления обьектами корзины

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    # @staticmethod
    # def get_item(pk):
    #     return Basket.objects.filter(pk=pk).first()

    def __str__(self):
        return f'Basket for {self.user.username} | Product {self.products.name}'

    def sum(self):
        return self.quantity * self.products.price

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)

    # первый способ переопределения методов модели
    # def delete(self):
    #     self.products.quantity += self.quantity
    #     self.products.save()
    #     super(self.__class__, self).delete()
    #
    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.products.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity  # закрутили шо капец,
    #         # не понятно как должно работать
    #     else:
    #         self.products.save()
    #         super(Basket, self).save(*args, **kwargs)
