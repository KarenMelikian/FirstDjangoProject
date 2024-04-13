from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from timeit import default_timer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from django.urls import reverse_lazy
from django.views.generic import (
                                  ListView,
                                  DetailView,
                                  DeleteView,
                                  UpdateView,
                                  CreateView,
                                  )

from .models import Product, Order
from .forms import GroupForm

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'runtime': default_timer()
    }

    return render(request, 'shop/index.html', context)


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


class ProductCreateView(LoginRequiredMixin, CreateView):
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



class GroupCreateView(LoginRequiredMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser

    template_name = 'shop/create-group.html'
    model = Group
    fields = 'name', 'permissions'
    success_url = reverse_lazy('groups')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
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


class OrderUpdateView(LoginRequiredMixin, UpdateView):
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



class GroupUpdateView(LoginRequiredMixin, UpdateView):
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



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser


    model = Product
    success_url = reverse_lazy('products')
    template_name = 'shop/product_confirm_delete.html'

class ProductArchiveView(LoginRequiredMixin, DeleteView):
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



class GroupDeleteView(LoginRequiredMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Group
    success_url = reverse_lazy('groups')
    template_name = 'shop/group_confirm_delete.html'
