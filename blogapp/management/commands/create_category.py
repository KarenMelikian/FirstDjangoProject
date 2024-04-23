from django.core.management import BaseCommand

from blogapp.models import Author, Category, Tag, Article

class Command(BaseCommand):
    '''
    Create category
    '''

    def handle(self, *args, **options):
        self.stdout.write('Create category')

        names = [
            'Technology',
            'Science',
            'Travel',
            'Fashion'
        ]

        for name in names:
            name_, create = Category.objects.get_or_create(
                name=name,
            )

            self.stdout.write(f'Create new category: {name}\n')

        self.stdout.write(self.style.SUCCESS('Category successfully created.'))