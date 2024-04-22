from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from timeit import default_timer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _, ngettext
from django.views.generic import (ListView, DetailView, DeleteView, UpdateView, CreateView)
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .models import Product, Order
from .forms import GroupForm
from .serializers import ProductSerializer, OrderSerializer

def index(request: HttpRequest) -> HttpResponse:
    welcome_text = _('Welcome to my shop!')
    context = {
        'runtime': default_timer(),
        'hello': welcome_text
    }

    return render(request, 'shop/index.html', context)


class ProductSetView(ModelViewSet):
    """
    A view set for interacting with the product resource.

    This view set provides CRUD (Create, Retrieve, Update, Delete) operations
    for the product resource. It supports listing all products, creating a new product,
    retrieving a specific product by ID, updating an existing product, and deleting a product.

    Attributes:
        queryset (QuerySet): The queryset representing all products in the database.
        serializer_class (Serializer): The serializer class used to serialize/deserialize
            product instances.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    search_fields = ["name", "description", ]
    filterset_fields = [
        "name",
        "description",
        "price",
        "discount",
        "is_archived"
    ]
    ordering_fields = [
        "name",
        "price",
        "discount",
    ]


class OrderSetView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    search_fields = [
        "delivery_address", 'user'
    ]

    filterset_fields = [
        'delivery_address',
        'promocode',
        'user'
    ]

    ordering_fields = [
        'created_at',
        'user'
    ]

class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'shop/product-list.html'
    model = Product
    context_object_name = 'products'

class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'shop/order-list.html'
    model = Order
    context_object_name = 'orders'

class GroupListView(LoginRequiredMixin, ListView):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': GroupForm,
            'groups': Group.objects.all()
        }
        return render(request, 'shop/group-list.html', context)

    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(request.path)


class ProductDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'shop/product-details.html'
    model = Product
    context_object_name = 'product'


class OrderDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'shop/order-details.html'
    model = Order
    context_object_name = 'order'



class GroupDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'shop/group-details.html'
    model = Group
    context_object_name = 'group'


class ProductCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser

    template_name = 'shop/create-product.html'
    model = Product
    fields = 'name', 'description', 'price', 'discount'
    success_url = reverse_lazy('products')



class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'shop/create-order.html'
    model = Order
    fields = 'delivery_address', 'promocode', 'user', 'products'
    success_url = reverse_lazy('orders')



class GroupCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser

    template_name = 'shop/create-group.html'
    model = Group
    fields = 'name', 'permissions'
    success_url = reverse_lazy('groups')


class ProductUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Product
    fields = 'name', 'description', 'price', 'discount'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'product_details',
            kwargs={'pk': self.object.pk}
        )


class OrderUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Order
    fields = 'delivery_address', 'promocode', 'products'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'order_details',
            kwargs={'pk': self.object.pk}
        )



class GroupUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser


    model = Group
    fields = 'name', 'permissions'
    template_name = 'shop/group_update_form.html'

    def get_success_url(self):
        return reverse(
            'group_details',
            kwargs={'pk': self.object.pk}
        )



class ProductDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser


    model = Product
    success_url = reverse_lazy('products')
    template_name = 'shop/product_confirm_delete.html'

class ProductArchiveView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser


    model = Product
    success_url = reverse_lazy('products')
    template_name = 'shop/product_confirm_archive.html'

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.is_archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('orders')



class GroupDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Group
    success_url = reverse_lazy('groups')
    template_name = 'shop/group_confirm_delete.html'
