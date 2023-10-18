from import_export import resources
from .models import Item


class ItemResources(resources.ModelResource):
    class Meta:
        model = Item
        fields = ('item_name', 'description', 'phone_or_email', 'created', 'updated', 'status')
