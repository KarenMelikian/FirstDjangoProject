from django.core.management import BaseCommand

from shop.models import Product


class Command(BaseCommand):
    '''
    Command to create products.

    This command creates sample products for demonstration purposes.

    Usage:
    python manage.py create_products
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
        self.stdout.write('Creating products...')

        names = [
            'Laptop',
            'Desktop',
            'Smartphone'
        ]

        prices = [
            1999,
            2999,
            999
        ]

        for name, price in zip(names, prices):
            product, created = Product.objects.get_or_create(
                name=name,
                price=price
            )
            self.stdout.write(f'Created product {name} for ${price}')

        self.stdout.write(self.style.SUCCESS('Products successfully created.'))

