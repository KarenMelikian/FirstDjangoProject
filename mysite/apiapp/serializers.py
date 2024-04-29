from django.contrib.auth.models import Group
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the Group model.

    This serializer serializes Group model instances to JSON format.

    Attributes:
        model: The model class to be serialized.
        fields: The fields to include in the serialized output.
    """
    class Meta:
        model = Group
        fields = 'pk', 'name'
