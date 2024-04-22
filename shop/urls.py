from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (index,
                    ProductListView,
                    OrderListView,
                    GroupListView,
                    ProductDetailsView,
                    OrderDetailsView,
                    GroupDetailsView,
                    ProductCreateView,
                    OrderCreateView,
                    GroupCreateView,
                    ProductUpdateView,
                    OrderUpdateView,
                    GroupUpdateView,
                    ProductDeleteView,
                    ProductArchiveView,
                    OrderDeleteView,
                    GroupDeleteView,
                    ProductSetView,
                    OrderSetView)

routers = DefaultRouter()

routers.register('products', ProductSetView)
routers.register('orders', OrderSetView)


urlpatterns = [
    path('', index, name='index'),
    path('api', include(routers.urls)),
    path('products/', ProductListView.as_view(), name='products'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('groups/', GroupListView.as_view(), name='groups'),
    path('product/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('order/<int:pk>/', OrderDetailsView.as_view(), name='order_details'),
    path('group/<int:pk>/', GroupDetailsView.as_view(), name='group_details'),
    path('create-product/', ProductCreateView.as_view(), name='create_product'),
    path('create-order/', OrderCreateView.as_view(), name='create_order'),
    path('create-group/', GroupCreateView.as_view(), name='create_group'),
    path('update-product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('update-order/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),
    path('update-group/<int:pk>/', GroupUpdateView.as_view(), name='update_group'),
    path('archive-product/<int:pk>/', ProductArchiveView.as_view(), name='archive_product'),
    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('delete-order/<int:pk>/', OrderDeleteView.as_view(), name='delete_order'),
    path('delete-group/<int:pk>/', GroupDeleteView.as_view(), name='delete_group')
]