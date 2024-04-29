from django.contrib.auth.models import Group
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import GroupSerializer

class FirstAPIView(ListAPIView):
    """
    API view for retrieving a list of groups.

    This view retrieves a list of all groups available in the system.

    Attributes:
        queryset (QuerySet): The queryset representing all groups in the system.
        serializer_class (Serializer): The serializer class used to serialize/deserialize group instances.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
