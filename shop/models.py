from django.db import models
from django.utils.timezone import now

from myauth.models import User
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'), max_length=500)
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2)
    discount = models.IntegerField(_('discount'), default=0)
    created_at = models.DateField(_('created_at'), default=now)
    is_archived = models.BooleanField(_('is_archived'), default=False)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return f'{self.name}: ID={self.pk}'


class Order(models.Model):
    delivery_address = models.CharField(_('delivery_address'), max_length=50)
    promocode = models.CharField(_('promocode'), max_length=10, default='')
    created_at = models.DateField(_('created_at'), default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='order')

    class Meta:
        db_table = 'order'