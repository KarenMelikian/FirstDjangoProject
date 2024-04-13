from django.core.management import BaseCommand

from shop.models import Product


class Command(BaseCommand):
    '''
    Create products
    '''


    def handle(self, *args, **options):
        self.stdout.write('Create products')

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
            name_, created = Product.objects.get_or_create(
                name = name,
                price = price
            )
            self.stdout.write(f'Create product {name} for ${price}')

        self.stdout.write(self.style.SUCCESS('Products successfully created. '))