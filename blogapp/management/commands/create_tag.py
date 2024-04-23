from django.core.management import BaseCommand

from blogapp.models import Author, Category, Tag, Article

class Command(BaseCommand):
    '''
    Create tags
    '''

    def handle(self, *args, **options):
        self.stdout.write('Create tags')

        names = [
            'Python',
            'Django',
            'Physics',
            'Biology',
            'Adventure',
            'Fashion Trends'
        ]



        for name in names:
            name_, create = Tag.objects.get_or_create(
                name=name,
            )

            self.stdout.write(f'Create new tag: {name}\n')

        self.stdout.write(self.style.SUCCESS('Tags successfully created.'))