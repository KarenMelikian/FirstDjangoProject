from django.db import models
from django.utils.timezone import now

from myauth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.IntegerField(default=0)
    created_at = models.DateField(default=now)
    is_archived = models.BooleanField(default=False)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return f'{self.name}: ID={self.pk}'


class Order(models.Model):
    delivery_address = models.CharField(max_length=50)
    promocode = models.CharField(max_length=10, default='')
    created_at = models.DateField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='order')

    class Meta:
        db_table = 'order'