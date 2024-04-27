from django.core.management import BaseCommand
from blogapp.models import Author, Category, Tag, Article

class Command(BaseCommand):
    """
    Management command for creating categories.

    This command creates new categories with specified names.

    Attributes:
        args (tuple): The positional arguments for the command.
        options (dict): The options for the command.
    """

    def handle(self, *args, **options):
        """
        Handles the execution of the management command.

        This method creates new categories with specified names.

        Args:
            args: The positional arguments for the command.
            options: The options for the command.
        """
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
