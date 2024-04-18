from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_image_to(instance, filename):
    return f'user_{instance.pk}/{filename}'


class User(AbstractUser):
    bio = models.TextField(_('Bio'), max_length=500, blank=True, null=True)
    age = models.IntegerField(_('Age'), blank=True, null=True)
    image = models.ImageField(_('Image'),
                              blank=True,
                              null=True,
                              upload_to=upload_image_to)


    class Meta:
        db_table = 'user'