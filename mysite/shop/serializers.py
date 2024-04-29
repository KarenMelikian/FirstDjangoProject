from rest_framework import serializers

from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    This serializer converts Product objects to JSON representations and vice versa.

    Attributes:
        pk (IntegerField): The primary key of the product.
        name (CharField): The name of the product.
        description (CharField): A brief description of the product.
        price (DecimalField): The price of the product.
        discount (IntegerField): The discount percentage applied to the product.
    """
    class Meta:
        model = Product
        fields = 'pk', 'name', 'description', 'price', 'discount'


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.

    This serializer converts Order objects to JSON representations and vice versa.

    Attributes:
        pk (IntegerField): The primary key of the order.
        delivery_address (CharField): The delivery address for the order.
        promocode (CharField): The promotional code applied to the order.
        user (PrimaryKeyRelatedField): The primary key of the user who placed the order.
        products (PrimaryKeyRelatedField): The primary keys of the products included in the order.
    """
    class Meta:
        model = Order
        fields = 'pk', 'delivery_address', 'promocode', 'user', 'products'
