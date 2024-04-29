from django.db import models
from django.utils.timezone import now

from myauth.models import User
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    """
    Model representing a product in the store.

    Attributes:
        name (str): The name of the product.
        description (str): A brief description of the product.
        price (Decimal): The price of the product.
        discount (int): The discount percentage applied to the product.
        created_at (Date): The date and time when the product was created.
        is_archived (bool): Indicates if the product is archived or not.
    """
    name = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'), max_length=500)
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2)
    discount = models.IntegerField(_('discount'), default=0)
    created_at = models.DateField(_('created_at'), default=now)
    is_archived = models.BooleanField(_('is_archived'), default=False)

    class Meta:
        db_table = 'product'

    def __str__(self):
        """
        Returns a string representation of the Product object.

        Returns:
            str: A string containing the name and ID of the product.
        """
        return f'{self.name}: ID={self.pk}'


class Order(models.Model):
    """
    Model representing an order in the store.

    Attributes:
        delivery_address (str): The delivery address for the order.
        promocode (str): The promotional code applied to the order.
        created_at (Date): The date and time when the order was created.
        user (User): The user who placed the order.
        products (ManyToManyField): The products included in the order.
    """
    delivery_address = models.CharField(_('delivery_address'), max_length=50)
    promocode = models.CharField(_('promocode'), max_length=10, default='')
    created_at = models.DateField(_('created_at'), default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='order')

    class Meta:
        db_table = 'order'