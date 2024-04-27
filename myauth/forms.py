from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import User

class UserRegistrationForm(UserCreationForm):
    """
    Form for user registration.

    This form extends the UserCreationForm provided by Django to include additional fields.

    Attributes:
        first_name (CharField): The field for the user's first name.
        last_name (CharField): The field for the user's last name.
        email (EmailField): The field for the user's email address.
    """
    first_name = forms.CharField(label=_('First Name'))
    last_name = forms.CharField(label=_('Last Name'))
    email = forms.EmailField(label=_('Email'))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
