from django.contrib import admin
from store.admin import ProductAdmin
from tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.
from store.models import Product
class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem
class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]
admin.site.unregister(Product)
admin.site.register(Product,CustomProductAdmin)