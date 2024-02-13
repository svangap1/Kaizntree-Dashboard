from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['sku', 'name', 'category', 'stock_status', 'available_stock']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['available_stock'] = float(instance.available_stock) if instance.available_stock is not None else None
        return representation
