from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Product, Order
from .admin_mixins import ExportAsCSVMixin


@admin.action(description='Product archiving')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_archived = True)

@admin.action(description='Product unarchiving')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_archived = False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv'
    ]


    list_display = 'name', 'description_short', 'price', 'discount', 'created_at', 'is_archived'
    list_display_links = 'name',
    search_fields = 'name',
    fieldsets = [(
        None, {
            'fields': ('name', 'description')
        }
    ),
        ('Price options', {
            'fields': ('price', 'discount'),
            'classes': ('collapse',)
        }),
        (None, {
            'fields': ('created_at', )
        }),
        ('Product archiving', {
            'fields': ('is_archived', ),
            'classes': ('collapse', )
        })]

    def description_short(self, obj: Product):
        if len(obj.description) < 48:
            return obj.description
        else:
            return obj.description[:48] + '...'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'delivery_address', 'promocode', 'created_at', 'user_verbose', 'product_display'

    def user_verbose(self, obj: Order):
        return obj.user.first_name or obj.user.username

    def product_display(self, obj: Order):
        products = [product.name for product in obj.products.all()]
        return ', '.join(products)