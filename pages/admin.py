from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Item



@admin.register(Item)
class ItemsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['author', 'item_name', 'phone_or_email', 'upload_image', 'status']
    list_filter = ['status', 'created', 'author']
    search_fields = ['item_name', 'description']
    raw_id_fields = ['author']
    date_hierarchy = 'created'
    ordering = ['status', 'created']