from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_image_to(instance, filename):
    """
    Function to generate upload path for user images.

    Args:
        instance (User): The User instance.
        filename (str): The original filename of the image.

    Returns:
        str: The upload path for the image.
    """
    return f'user_{instance.pk}/{filename}'

class User(AbstractUser):
    """
    Custom user model.

    This model extends the AbstractUser model provided by Django to add additional fields.

    Attributes:
        bio (TextField): The user's biography.
        age (IntegerField): The user's age.
        image (ImageField): The user's profile image.
    """
    bio = models.TextField(_('Bio'), max_length=500, blank=True, null=True)
    age = models.IntegerField(_('Age'), blank=True, null=True)
    image = models.ImageField(_('Image'),
                              blank=True,
                              null=True,
                              upload_to=upload_image_to)

    class Meta:
        db_table = 'user'
