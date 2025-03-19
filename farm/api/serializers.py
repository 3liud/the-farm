from rest_framework import serializers

from .models import County, Item, ItemCategory


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ["id", "name"]


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ["id", "name"]


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Item
        fields = ["id", "name", "category"]
