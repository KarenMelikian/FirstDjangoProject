from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'



class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'



class Tag(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'



class Article(models.Model):
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