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
    """
    View function for the index page of the shop.

    Displays a welcome message and renders the index.html template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
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
    """
    A view set for interacting with the order resource.

    This view set provides CRUD (Create, Retrieve, Update, Delete) operations
    for the order resource. It supports listing all orders, creating a new order,
    retrieving a specific order by ID, updating an existing order, and deleting an order.

    Attributes:
        queryset (QuerySet): The queryset representing all orders in the database.
        serializer_class (Serializer): The serializer class used to serialize/deserialize
            order instances.
    """
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
    """
    View for listing all products.

    This view displays a list of all products available in the store.

    Attributes:
        template_name (str): The name of the template used to render the view.
        model (Model): The model associated with this view (Product).
        context_object_name (str): The variable name used in the template to access the list of products.
    """
    template_name = 'shop/product-list.html'
    model = Product
    context_object_name = 'products'

class OrderListView(LoginRequiredMixin, ListView):
    """
    View for listing all orders.

    This view displays a list of all orders placed in the store.

    Attributes:
        template_name (str): The name of the template used to render the view.
        model (Model): The model associated with this view (Order).
        context_object_name (str): The variable name used in the template to access the list of orders.
    """
    template_name = 'shop/order-list.html'
    model = Order
    context_object_name = 'orders'

class GroupListView(LoginRequiredMixin, ListView):
    """
    View for listing all user groups.

    This view displays a list of all user groups in the system.

    Attributes:
        template_name (str): The name of the template used to render the view.
    """
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
    """
    View for displaying details of a product.

    This view displays detailed information about a specific product.

    Attributes:
        template_name (str): The name of the template used to render the view.
        model (Model): The model associated with this view (Product).
        context_object_name (str): The variable name used in the template to access the product object.
    """
    template_name = 'shop/product-details.html'
    model = Product
    context_object_name = 'product'


class OrderDetailsView(LoginRequiredMixin, DetailView):
    """
    View for displaying details of an order.

    This view displays detailed information about a specific order.

    Attributes:
        template_name (str): The name of the template used to render the view.
        model (Model): The model associated with this view (Order).
        context_object_name (str): The variable name used in the template to access the order object.
    """
    template_name = 'shop/order-details.html'
    model = Order
    context_object_name = 'order'



class GroupDetailsView(LoginRequiredMixin, DetailView):
    """
    View for displaying details of a user group.

    This view displays detailed information about a specific user group.

    Attributes:
        template_name (str): The name of the template used to render the view.
        model (Model): The model associated with this view (Group).
        context_object_name (str): The variable name used in the template to access the group object.
    """
    template_name = 'shop/group-details.html'
    model = Group
    context_object_name = 'group'


class ProductCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    """
    View for creating a new product.

    This view allows superusers to create new products.

    Attributes:
        template_name (str): The name of the template used to render the view.
        model (Model): The model associated with this view (Product).
        fields (tuple): The fields of the model to be included in the form.
        success_url (str): The URL to redirect to after successfully creating the product.
    """
    def test_func(self):
        return self.request.user.is_superuser

    template_name = 'shop/create-product.html'
    model = Product
    fields = 'name', 'description', 'price', 'discount'
    success_url = reverse_lazy('products')



class OrderCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new order.

    This view allows authenticated users to create new orders.

    Attributes:
        template_name (str): The name of the template used to render the view.
        model (Model): The model associated with this view (Order).
        fields (tuple): The fields of the model to be included in the form.
        success_url (str): The URL to redirect to after successfully creating the order.
    """
    template_name = 'shop/create-order.html'
    model = Order
    fields = 'delivery_address', 'promocode', 'user', 'products'
    success_url = reverse_lazy('orders')



class GroupCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    """
    View for creating a new user group.

    This view allows superusers to create new user groups.

    Attributes:
        template_name (str): The name of the template used to render the view.
        model (Model): The model associated with this view (Group).
        fields (tuple): The fields of the model to be included in the form.
        success_url (str): The URL to redirect to after successfully creating the user group.
    """
    def test_func(self):
        return self.request.user.is_superuser

    template_name = 'shop/create-group.html'
    model = Group
    fields = 'name', 'permissions'
    success_url = reverse_lazy('groups')


class ProductUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    """
    View for updating an existing product.

    This view allows superusers to update existing products.

    Attributes:
        model (Model): The model associated with this view (Product).
        fields (tuple): The fields of the model to be included in the form.
        template_name_suffix (str): The suffix to append to the template name.
    """
    def test_func(self):
        return self.request.user.is_superuser

    model = Product
    fields = 'name', 'description', 'price', 'discount'
    template_name_suffix = '_update_form'


class OrderUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    """
    View for updating an existing order.

    This view allows superusers to update existing orders.

    Attributes:
        model (Model): The model associated with this view (Order).
        fields (tuple): The fields of the model to be included in the form.
        template_name_suffix (str): The suffix to append to the template name.
    """
    def test_func(self):
        return self.request.user.is_superuser

    model = Order
    fields = 'delivery_address', 'promocode', 'products'
    template_name_suffix = '_update_form'


class GroupUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    """
    View for updating an existing user group.

    This view allows superusers to update existing user groups.

    Attributes:
        model (Model): The model associated with this view (Group).
        fields (tuple): The fields of the model to be included in the form.
        template_name (str): The name of the template used to render the view.
    """
    def test_func(self):
        return self.request.user.is_superuser


    model = Group
    fields = 'name', 'permissions'
    template_name = 'shop/group_update_form.html'



class ProductDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    View for deleting a product.

    This view allows superusers to delete products.

    Attributes:
        model (Model): The model associated with this view (Product).
        success_url (str): The URL to redirect to after successfully deleting the product.
        template_name (str): The name of the template used to render the delete confirmation page.
    """
    def test_func(self):
        return self.request.user.is_superuser


    model = Product
    success_url = reverse_lazy('products')
    template_name = 'shop/product_confirm_delete.html'

class ProductArchiveView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    View for archiving a product.

    This view allows superusers to archive products.

    Attributes:
        model (Model): The model associated with this view (Product).
        success_url (str): The URL to redirect to after successfully archiving the product.
        template_name (str): The name of the template used to render the archive confirmation page.
    """
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
    """
    View for deleting an order.

    This view allows authenticated users to delete their own orders.

    Attributes:
        model (Model): The model associated with this view (Order).
        success_url (str): The URL to redirect to after successfully deleting the order.
    """
    model = Order
    success_url = reverse_lazy('orders')



class GroupDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    View for deleting a user group.

    This view allows superusers to delete user groups.

    Attributes:
        model (Model): The model associated with this view (Group).
        success_url (str): The URL to redirect to after successfully deleting the user group.
        template_name (str): The name of the template used to render the delete confirmation page.
    """
    def test_func(self):
        return self.request.user.is_superuser

    model = Group
    success_url = reverse_lazy('groups')
    template_name = 'shop/group_confirm_delete.html'
