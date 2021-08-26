from django.contrib import admin
from ecommerce.models import Items, Category, Subcategory, Order, OrderedItem, Address


# Register your models here.
@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(OrderedItem)
admin.site.register(Order)
admin.site.register(Address)
