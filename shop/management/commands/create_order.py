from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shop.models import Product, Order


class Command(BaseCommand):
    '''
    Command to create orders.

    This command creates sample orders for demonstration purposes.

    Usage:
    python manage.py create_orders
    '''

    def handle(self, *args, **options):
        """
        Handles the execution of the command.

        Args:
            *args: Variable length argument list.
            **options: Keyword arguments.

        Returns:
            None
        """
        self.stdout.write('Creating orders...')

        user = User.objects.get(pk=1)
        product1 = Product.objects.get(pk=1)
        product2 = Product.objects.get(pk=3)

        order, created = Order.objects.get_or_create(
            delivery_address='ASD465AS',
            user=user,
        )
        order.products.add(product1, product2)

        self.stdout.write(self.style.SUCCESS('Orders successfully created.'))
