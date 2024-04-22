from django.contrib.auth.models import Group
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializers import GroupSerializer

class FirstAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer