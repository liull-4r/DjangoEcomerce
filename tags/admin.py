from django.contrib import admin
from . models import Tag, TaggedItem

# Register your models here.
admin.site.register(TaggedItem)

@admin.register(Tag)
class tagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
