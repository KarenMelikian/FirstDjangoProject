from django.db import models

class Author(models.Model):
    """
    Model representing an author.

    Attributes:
        name (CharField): The name of the author.
        bio (TextField): The biography of the author.
    """
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'

class Category(models.Model):
    """
    Model representing a category.

    Attributes:
        name (CharField): The name of the category.
    """
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'

class Tag(models.Model):
    """
    Model representing a tag.

    Attributes:
        name (CharField): The name of the tag.
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'

class Article(models.Model):
    """
    Model representing an article.

    Attributes:
        title (CharField): The title of the article.
        content (TextField): The content of the article.
        pub_date (DateTimeField): The publication date of the article.
        author (ForeignKey): The author of the article.
        category (ForeignKey): The category of the article.
        tags (ManyToManyField): The tags associated with the article.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='article')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
