from django.urls import path

from .views import FirstAPIView

urlpatterns = [
    path('', FirstAPIView.as_view(), name='first')
]