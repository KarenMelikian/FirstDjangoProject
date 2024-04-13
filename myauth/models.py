from django.contrib.auth.models import AbstractUser
from django.db import models


def upload_image_to(instance, filename):
    return f'user_{instance.pk}/{filename}'


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True,
                              null=True,
                              upload_to=upload_image_to)


    class Meta:
        db_table = 'user'