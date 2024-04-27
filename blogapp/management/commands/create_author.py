from django.core.management import BaseCommand
from blogapp.models import Author, Category, Tag, Article

class Command(BaseCommand):
    """
    Management command for creating authors.

    This command creates new authors with specified names and biographies.

    Attributes:
        args (tuple): The positional arguments for the command.
        options (dict): The options for the command.
    """

    def handle(self, *args, **options):
        """
        Handles the execution of the management command.

        This method creates new authors with specified names and biographies.

        Args:
            args: The positional arguments for the command.
            options: The options for the command.
        """
        self.stdout.write('Create author')

        names = [
            'John Doe',
            'Jane Smith',
            'Alex Johnson'
        ]

        bios = [
            'Some bio about John Doe',
            'Some bio about Jane Smith',
            'Some bio about Alex Johnson'
        ]

        for name, bio in zip(names, bios):
            name_, create = Author.objects.get_or_create(
                name=name,
                bio=bio
            )

            self.stdout.write(f'Create new author\nname: {name}\nbio: {bio}')

        self.stdout.write(self.style.SUCCESS('Author successfully created.'))
