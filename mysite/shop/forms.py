from django import forms
from django.contrib.auth.models import Group

from .models import Product, Order

class ProductForm(forms.ModelForm):
    """
    Form for creating or updating a product.

    This form allows users to input details for creating or updating a product.

    Attributes:
        name (CharField): The name of the product.
        description (CharField): A brief description of the product.
        price (DecimalField): The price of the product.
        discount (IntegerField): The discount percentage applied to the product.
    """
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'discount']


class OrderForm(forms.ModelForm):
    """
    Form for creating or updating an order.

    This form allows users to input details for creating or updating an order.

    Attributes:
        delivery_address (CharField): The delivery address for the order.
        promocode (CharField): The promotional code applied to the order.
        user (ModelChoiceField): The user who placed the order.
        products (ModelMultipleChoiceField): The products included in the order.
    """
    class Meta:
        model = Order
        fields = ['delivery_address', 'promocode', 'user', 'products']


class GroupForm(forms.ModelForm):
    """
    Form for creating or updating a user group.

    This form allows users to input details for creating or updating a user group.

    Attributes:
        name (CharField): The name of the user group.
        permissions (ModelMultipleChoiceField): The permissions associated with the user group.
    """
    class Meta:
        model = Group
        fields = ['name', 'permissions']
