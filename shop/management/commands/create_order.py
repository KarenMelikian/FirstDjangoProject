from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shop.models import Product, Order


class Command(BaseCommand):
    '''
    Create orders
    '''

    def handle(self, *args, **options):
        self.stdout.write('Create orders')

        user = User.objects.get(pk=1)
        product1 = Product.objects.get(pk=1)
        product2 = Product.objects.get(pk=3)

        name, created = Order.objects.get_or_create(
            delivery_address = 'ASD465AS',
            user = user,
        )
        name.products.add(product1, product2)

        self.stdout.write(self.style.SUCCESS('Orders successfully created. '))