from django.db import models

from django.conf import settings
from mainapp.models import Product


# Create your models here.

# второй способ переопределения/ удаления набора обьектов
class OrdersQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.products.quantity += object.quantity
            object.products.save()
        super(OrdersQuerySet, self).delete(*args, **kwargs)


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен на обработку'),
        (PROCEEDED, 'обрабатывается'),
        (PAID, 'оплачен'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=ORDER_STATUS_CHOICES, default=FORMING, verbose_name='статус')
    created = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='обновлен')
    is_active = models.BooleanField(default=True, verbose_name='активен')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Текущий заказ: {self.id}'

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_products_type_quantity(self):
        items = self.orderitems.select_related()
        return len(items)

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.products.price, items)))

    def delete(self):
        for item in self.orderitems.select_related():
            item.products.quantity += item.quantity
            item.products.save()

        self.is_active = False
        self.save()


class OrderItem(models.Model):
    objects = OrdersQuerySet.as_manager()  # вызов

    order = models.ForeignKey(Order,
                              related_name='orderitems',
                              on_delete=models.CASCADE)
    products = models.ForeignKey(Product,
                                 verbose_name='продукт',
                                 on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')

    # @staticmethod
    # def get_item(pk):
    #     return OrderItem.objects.filter(pk=pk).first()

    def get_products_cost(self):
        return self.products.price * self.quantity

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return f'Бланк заказа: {self.id}'

# удаление обьекта из корзины
# def delete(self, using=None, keep_parents=False):
#     self.product.quantity += self.quantity
#     self.product.save()
#     super(self.__class__, self).delete()
