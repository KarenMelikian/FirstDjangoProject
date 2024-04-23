from django.core.management import BaseCommand

from blogapp.models import Author, Category, Tag, Article
from django.db import transaction
class Command(BaseCommand):
    '''
    Create article
    '''

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Create article')


        # Authors
        john_doe = Author.objects.get(pk=1)
        jane_smith = Author.objects.get(pk=2)
        alex_johnson = Author.objects.get(pk=3)


        # Categories
        technology = Category.objects.get(pk=1)
        science = Category.objects.get(pk=2)
        travel = Category.objects.get(pk=3)
        fashion = Category.objects.get(pk=4)

        # tags
        python = Tag.objects.get(pk=1)
        django = Tag.objects.get(pk=2)
        physics = Tag.objects.get(pk=3)
        biology = Tag.objects.get(pk=4)
        adventure = Tag.objects.get(pk=5)

        title1 = 'Introduction to Django'
        title2 = 'The Theory of Relativity'
        title3 = 'Exploring the Grand Canyon'


        content1 = 'Some content about Django.'
        content2 = 'Some content about the theory of relativity.'
        content3 = 'Some content about exploring the Grand Canyon.'

        name_, create = Article.objects.get_or_create(
            title = title3,
            content = content3,
            author = alex_johnson,
            category = travel
        )

        name_.tags.add(adventure)

        self.stdout.write(f'Create new article\n'
                          f'Title: {title3}\n')

