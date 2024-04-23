from django.core.management import BaseCommand

from blogapp.models import Author, Category, Tag, Article

class Command(BaseCommand):
    '''
    Create author
    '''

    def handle(self, *args, **options):
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