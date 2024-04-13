from django import forms
from django.contrib.auth.models import Group

from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'discount']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_address', 'promocode', 'user', 'products']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']