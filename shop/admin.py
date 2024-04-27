from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Product, Order
from .admin_mixins import ExportAsCSVMixin


@admin.action(description='Product archiving')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    """
    Admin action to mark selected products as archived.

    Args:
        modeladmin (ModelAdmin): The admin class instance.
        request (HttpRequest): The HTTP request.
        queryset (QuerySet): The queryset containing the selected products.
    """
    queryset.update(is_archived=True)

@admin.action(description='Product unarchiving')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    """
    Admin action to mark selected products as unarchived.

    Args:
        modeladmin (ModelAdmin): The admin class instance.
        request (HttpRequest): The HTTP request.
        queryset (QuerySet): The queryset containing the selected products.
    """
    queryset.update(is_archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    """
    Admin configuration for the Product model.

    This class defines how the Product model is displayed and managed in the Django admin interface.

    Attributes:
        actions (list): The list of available admin actions.
        list_display (tuple): The fields to display in the product list view.
        list_display_links (tuple): The fields to link to the product details view.
        search_fields (tuple): The fields to search for products.
        fieldsets (list): The fieldsets to organize the product detail view.
    """
    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv'
    ]

    list_display = 'name', 'description_short', 'price', 'discount', 'created_at', 'is_archived'
    list_display_links = 'name',
    search_fields = 'name',
    fieldsets = [
        (None, {'fields': ('name', 'description')}),
        ('Price options', {'fields': ('price', 'discount'), 'classes': ('collapse',)}),
        (None, {'fields': ('created_at',)}),
        ('Product archiving', {'fields': ('is_archived',), 'classes': ('collapse',)})
    ]

    def description_short(self, obj: Product):
        """
        Returns a shortened version of the product description.

        Args:
            obj (Product): The Product instance.

        Returns:
            str: Shortened description or full description if less than 48 characters.
        """
        if len(obj.description) < 48:
            return obj.description
        else:
            return obj.description[:48] + '...'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Order model.

    This class defines how the Order model is displayed and managed in the Django admin interface.

    Attributes:
        list_display (tuple): The fields to display in the order list view.
    """
    list_display = 'delivery_address', 'promocode', 'created_at', 'user_verbose', 'product_display'

    def user_verbose(self, obj: Order):
        """
        Returns the user's first name or username for display in the admin interface.

        Args:
            obj (Order): The Order instance.

        Returns:
            str: The user's first name or username.
        """
        return obj.user.first_name or obj.user.username

    def product_display(self, obj: Order):
        """
        Returns a comma-separated list of product names for display in the admin interface.

        Args:
            obj (Order): The Order instance.

        Returns:
            str: Comma-separated list of product names.
        """
        products = [product.name for product in obj.products.all()]
        return ', '.join(products)
